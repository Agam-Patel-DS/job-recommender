import os
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle


# Global Variables
vectorizer = None


def load_data(raw_data_dir):
    """
    Load raw data from the specified directory.

    Parameters:
    - raw_data_dir: Path to the directory containing raw data files.

    Returns:
    - A dictionary of loaded dataframes.
    """
    files = {
        "job_skills": "job_skills.csv",
        "job_summary": "job_summary.csv",
        "linkedin_jobs": "linkedin_job_postings.csv",
    }
    data = {}
    for key, file_name in files.items():
        file_path = os.path.join(raw_data_dir, file_name)
        data[key] = pd.read_csv(file_path)
    return data


def merge_and_clean_data(data):
    """
    Merge and clean the dataframes for preprocessing.

    Parameters:
    - data: Dictionary of dataframes (job_skills, job_summary, linkedin_jobs).

    Returns:
    - A cleaned and merged dataframe.
    """
    # Merge job_skills and job_summary using 'Job link'
    merged_df = pd.merge(data['job_skills'], data['job_summary'], on="job_link", how="inner")

    # Merge with linkedin_jobs using 'job_link'
    final_df = pd.merge(merged_df, data['linkedin_jobs'], left_on="job_link", right_on="job_link", how="inner")

    # Select relevant columns
    final_df = final_df[['job_link', 'job_title', 'company', 'job_location', 'job_skills', 'job_summary']]
    # final_df.rename(columns={"Job Skills": "job_skills", "Job Summary": "job_summary"}, inplace=True)

    # Clean text columns
    final_df['job_skills'] = final_df['job_skills'].fillna("").apply(lambda x: x.strip().lower())
    final_df['job_summary'] = final_df['job_summary'].fillna("").apply(lambda x: x.strip().lower())
    final_df['job_title'] = final_df['job_title'].fillna("").apply(lambda x: x.strip().lower())

    # Combine text columns for context
    final_df['combined_text'] = (
        final_df['job_title'] + " " + final_df['job_skills'] + " " + final_df['job_summary']
    )

    # Tokenize skills
    final_df['skills_list'] = final_df['job_skills'].apply(
        lambda x: [skill.strip() for skill in x.split(",") if skill.strip()]
    )

    # Remove duplicates
    final_df = final_df.drop_duplicates(subset=['job_link', 'combined_text'], keep='first').reset_index(drop=True)

    return final_df


def save_processed_data(processed_df, processed_data_dir):
    """
    Save the processed data to the target directory.

    Parameters:
    - processed_df: The processed dataframe to save.
    - processed_data_dir: Directory where processed data will be stored.
    """
    os.makedirs(processed_data_dir, exist_ok=True)
    target_file = os.path.join(processed_data_dir, "processed_jobs.csv")
    processed_df.to_csv(target_file, index=False)
    print(f"Processed data saved to: {target_file}")


def generate_embeddings(processed_df, processed_data_dir):
    """
    Generate TF-IDF embeddings for the combined text column and save them.

    Parameters:
    - processed_df: The dataframe containing the 'combined_text' column.
    - processed_data_dir: Directory where embeddings and vectorizer will be stored.
    """
    global vectorizer
    vectorizer = TfidfVectorizer(max_features=5000)
    embeddings = vectorizer.fit_transform(processed_df['combined_text'])

    # Save vectorizer and embeddings
    vectorizer_file = os.path.join(processed_data_dir, "tfidf_vectorizer.pkl")
    embeddings_file = os.path.join(processed_data_dir, "tfidf_embeddings.pkl")

    with open(vectorizer_file, "wb") as f:
        pickle.dump(vectorizer, f)
    with open(embeddings_file, "wb") as f:
        pickle.dump(embeddings, f)

    print("TF-IDF embeddings and vectorizer saved successfully.")


def get_embeddings(text_list, processed_data_dir):
    """
    Get TF-IDF embeddings for new text data using the saved vectorizer.

    Parameters:
    - text_list: List of strings to embed.
    - processed_data_dir: Directory containing the saved vectorizer.

    Returns:
    - TF-IDF embeddings for the given text data.
    """
    global vectorizer
    if not vectorizer:
        vectorizer_file = os.path.join(processed_data_dir, "tfidf_vectorizer.pkl")
        with open(vectorizer_file, "rb") as f:
            vectorizer = pickle.load(f)

    embeddings = vectorizer.transform(text_list)
    return embeddings


def preprocess(preprocess_config):
    """
    Run all preprocessing steps in sequence: load data, clean and merge, save processed data, and generate embeddings.

    Parameters:
    - raw_data_dir: Path to the directory containing raw data files.
    - processed_data_dir: Path to the directory where processed data will be stored.
    """
    raw_data_dir=preprocess_config.raw_data_dir
    processed_data_dir=preprocess_config.processed_data_dir
    model_dir=preprocess_config.model_dir

    print("Loading raw data...")
    raw_data = load_data(raw_data_dir)
    print("Raw data loaded successfully.")

    print("Merging and cleaning data...")
    processed_data = merge_and_clean_data(raw_data)
    print("Data merged and cleaned successfully.")

    print("Saving processed data...")
    save_processed_data(processed_data, processed_data_dir)

    print("Generating TF-IDF embeddings...")
    generate_embeddings(processed_data, model_dir)
    print("Preprocessing pipeline completed successfully.")
