import os

def create_project_structure(base_dir):
    """
    Create the modular folder structure for the 'job-recommender' GitHub repository.
    
    Args:
        base_dir (str): The base directory where the structure will be created.
    """
    # Define the folder structure relative to the base directory
    structure = [
        "data/raw",
        "data/processed",
        "src/data_processing",
        "src/recommendation",
        "utils",
        "app",
        "tests",
    ]
    
    # Define the files with their respective placeholder content
    files = {
        "main.py": "# Entry point for the Job Recommender System\n",
        "data/__init__.py": "",
        "data/raw/README.md": "# Raw data folder\nPlace raw datasets here.\n",
        "data/processed/README.md": "# Processed data folder\nPlace processed datasets here.\n",
        "src/__init__.py": "",
        "src/data_processing/__init__.py": "",
        "src/data_processing/data_ingestion.py": "# Module to handle data ingestion from Kaggle\n",
        "src/data_processing/preprocess_data.py": "# Module to preprocess the dataset\n",
        "src/recommendation/__init__.py": "",
        "src/recommendation/similarity_model.py": "# Module for similarity models (e.g., TF-IDF, Cosine Similarity)\n",
        "src/recommendation/recommend.py": "# Module for job recommendation logic\n",
        "utils/__init__.py": "",
        "utils/logger.py": "# Module for logging configuration\n",
        "utils/exceptions.py": "# Module for custom exceptions\n",
        "utils/config.py": "# Configuration file for paths and hyperparameters\n",
        "app/__init__.py": "",
        "app/streamlit_app.py": "# Streamlit app for the Job Recommender System\n",
        "tests/__init__.py": "",
        "tests/test_preprocess_data.py": "# Unit tests for preprocess_data.py\n",
        "tests/test_recommend.py": "# Unit tests for recommend.py\n",
    }
    
    # Ensure the base directory exists
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Create directories in the defined structure
    for folder in structure:
        folder_path = os.path.join(base_dir, folder)
        os.makedirs(folder_path, exist_ok=True)
    
    # Create files with placeholder content
    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, "w") as file:
            file.write(content)
    
    print(f"Project structure for 'job-recommender' created successfully under {base_dir}")


if __name__ == "__main__":
    # Define the base directory where the project structure will be created
    base_directory = "."
    
    # Create the structure
    create_project_structure(base_directory)
