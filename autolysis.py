import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import requests
import json
import numpy as np
import time
import subprocess

# Set your AI Proxy Token (ensure it's set in the environment before running)
AIPROXY_TOKEN = os.getenv("AIPROXY_TOKEN")
assert AIPROXY_TOKEN, "AIPROXY_TOKEN environment variable is required"

# Function to send requests to the AI Proxy endpoint
def query_openai(prompt: str, model="gpt-4o-mini"):
    url = "https://aiproxy.sanand.workers.dev/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {AIPROXY_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 1000
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content']
    except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
        print(f"Error occurred: {e}. Retrying...")
        time.sleep(5)  # Wait before retrying
        raise  # Re-raise the exception to trigger the retry mechanism

def load_dataset(filename: str):
    try:
        df = pd.read_csv(filename, encoding='utf-8')
    except UnicodeDecodeError:
        # Retry with a common fallback encoding
        df = pd.read_csv(filename, encoding='latin1')
    
    # Replace spaces in column names with underscores
    df.columns = df.columns.str.replace(' ', '_')
    
    return df

# Function to get relevant columns for correlation
def get_relevant_columns_for_correlation(df: pd.DataFrame):
    # Create a prompt asking for relevant columns for correlation analysis
    columns_list = ", ".join(df.columns)
    summary_statistics = df.describe(include='all').to_string()

    prompt = f"""
    I have the following columns in my dataset: {columns_list}.
    Here are the summary statistics of my dataset:
    {summary_statistics}

    Please provide a simple list of the relevant columns for correlation analysis based on the dataset provided.
    Consider both the column names and the summary statistics in your decision.
    The columns should be returned as a comma-separated list with no additional explanation.
    """
    return query_openai(prompt)

# Function to get relevant columns for histogram
def get_relevant_columns_for_histogram(df: pd.DataFrame):
    # Create a prompt asking for relevant columns for histogram analysis, including summary statistics
    columns_list = ", ".join(df.columns)
    summary_statistics = df.describe(include='all').to_string()

    prompt = f"""
    I have the following columns in my dataset: {columns_list}.
    Here are the summary statistics of my dataset:
    {summary_statistics}

    Please provide a simple list of the relevant columns for generating a histogram based on the dataset provided.
    Consider both the column names and the summary statistics in your decision.
    The columns should be returned as a comma-separated list with no additional explanation.
    """
    return query_openai(prompt)

# Function to get relevant columns for missing values heatmap
def get_relevant_columns_for_heatmap(df: pd.DataFrame):
    # Create a prompt asking for relevant columns for missing values heatmap analysis, including summary statistics
    columns_list = ", ".join(df.columns)
    summary_statistics = df.describe(include='all').to_string()

    prompt = f"""
    I have the following columns in my dataset: {columns_list}.
    Here are the summary statistics of my dataset:
    {summary_statistics}

    Please provide a simple list of the relevant columns for generating a missing values heatmap based on the dataset provided.
    Consider both the column names and the summary statistics in your decision.
    The columns should be returned as a comma-separated list with no additional explanation.
    """
    return query_openai(prompt)

# Function to parse the columns returned by the model
def parse_columns_from_response(response: str):
    # Clean and split the response into a list of columns
    response = response.strip().replace("\n", "").replace(" ", "")
    columns = response.split(",")  # This assumes the response is comma-separated
    return columns

# Function to detect outliers using z-scores
def detect_outliers(df: pd.DataFrame):
    numeric_df = df.select_dtypes(include=np.number)
    z_scores = np.abs((numeric_df - numeric_df.mean()) / numeric_df.std())
    outliers = (z_scores > 3).sum()
    return outliers

# Function to calculate the correlation values between pairs of relevant columns
def calculate_correlations(df: pd.DataFrame, relevant_columns: list):
    correlation_matrix = df[relevant_columns].corr()
    correlation_values = correlation_matrix.to_dict()  # Converts the matrix to a dictionary
    return correlation_values

# Function to generate a correlation plot
def create_correlation_plot(correlation_matrix: pd.DataFrame, output_filename: str):
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt='.2f')
    plt.title("Correlation Matrix")
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()

# Function to generate a histogram for numeric columns
def create_histogram(df: pd.DataFrame, output_filename: str):
    numeric_columns = df.select_dtypes(include=np.number).columns
    df[numeric_columns].hist(figsize=(12, 10), bins=15, edgecolor='black')
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()

# Function to generate a heatmap for missing values
def create_missing_values_heatmap(df: pd.DataFrame, output_filename: str):
    plt.figure(figsize=(12, 8))
    sns.heatmap(df.isnull(), cbar=False, cmap="viridis")
    plt.title("Missing Values Heatmap")
    plt.tight_layout()
    plt.savefig(output_filename)
    plt.close()

# Function to prompt the LLM for analysis and storytelling
def generate_story(df: pd.DataFrame, summary, outliers, correlation_values):
    prompt = f"""
    I have the following dataset:

    Columns: {', '.join(df.columns)}
    Summary statistics: {summary.to_string()}
    Outlier counts: {outliers.to_string()}
    
    Here are the correlations between the relevant columns for correlation analysis:
    {json.dumps(correlation_values, indent=2)}

    Please analyze the data, identify interesting insights, trends, or anomalies, and narrate a story. Provide implications of the findings and suggest potential actions.
    """
    return query_openai(prompt)

# Main function to process the CSV and generate outputs
def main(dataset_file: str):
    # Load the dataset
    df = load_dataset(dataset_file)

    # Get the relevant columns for each analysis type
    response_correlation = get_relevant_columns_for_correlation(df)
    relevant_columns_correlation = parse_columns_from_response(response_correlation)

    response_histogram = get_relevant_columns_for_histogram(df)
    relevant_columns_histogram = parse_columns_from_response(response_histogram)

    response_heatmap = get_relevant_columns_for_heatmap(df)
    relevant_columns_heatmap = parse_columns_from_response(response_heatmap)

    # Check if all the columns returned exist in the dataset
    existing_columns_correlation = [col for col in relevant_columns_correlation if col in df.columns]
    existing_columns_histogram = [col for col in relevant_columns_histogram if col in df.columns]
    existing_columns_heatmap = [col for col in relevant_columns_heatmap if col in df.columns]

    # Filter the dataset based on the relevant columns
    df_filtered_correlation = df[existing_columns_correlation]
    df_filtered_histogram = df[existing_columns_histogram]
    df_filtered_heatmap = df[existing_columns_heatmap]

    # Analyze the data
    summary = df.describe(include='all')
    outliers = detect_outliers(df)

    # Calculate the correlations for the relevant columns and generate the correlation plot
    correlation_values = calculate_correlations(df, existing_columns_correlation)
    correlation_matrix = df[existing_columns_correlation].corr()
    correlation_plot_file = "correlation_plot.png"
    create_correlation_plot(correlation_matrix, correlation_plot_file)

    # Generate a histogram for the relevant columns
    histogram_file = "histogram.png"
    create_histogram(df_filtered_histogram, histogram_file)

    # Generate a heatmap for missing values
    missing_values_heatmap_file = "missing_values_heatmap.png"
    create_missing_values_heatmap(df_filtered_heatmap, missing_values_heatmap_file)

    # Generate the story from the LLM with the correlation values included
    story = generate_story(df, summary, outliers, correlation_values)

    # Save the analysis in a README.md file
    readme_filename = "README.md"
    with open(readme_filename, "w") as readme_file:
        readme_file.write(f"# Data Analysis Story for {dataset_file}\n\n")
        readme_file.write("## Summary Statistics\n")
        readme_file.write(summary.to_string())
        readme_file.write("\n\n## Outlier Counts\n")
        readme_file.write(outliers.to_string())
        readme_file.write("\n\n## Story and Insights\n")
        readme_file.write(story)
        readme_file.write("\n\n## Visualizations\n")
        readme_file.write(f"### Correlation Plot\n![Correlation Plot]({correlation_plot_file})\n")
        readme_file.write(f"### Histogram\n![Histogram]({histogram_file})\n")
        readme_file.write(f"### Missing Values Heatmap\n![Missing Values Heatmap]({missing_values_heatmap_file})\n")

# Entry point when script is executed
if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python autolysis.py <dataset.csv>")
        sys.exit(1)

    dataset_file = sys.argv[1]

    # Retry mechanism for the main function
    while True:
        try:
            main(dataset_file)
            break  # Exit the loop if no errors occurred
        except (requests.exceptions.ConnectionError, requests.exceptions.HTTPError) as e:
            print(f"Error occurred: {e}. Retrying...")
            time.sleep(5)  # Wait before retrying
            subprocess.run(["uv", "run", "autolysis.py", dataset_file], check=True)
            break
