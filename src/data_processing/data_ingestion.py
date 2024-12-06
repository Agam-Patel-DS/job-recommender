import os
import subprocess
from zipfile import ZipFile

def download_dataset(kaggle_dataset: str, download_dir: str):
    # Ensure the directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    
    print("Downloading dataset...")
    # Command to download and unzip the dataset
    command = f"kaggle datasets download {kaggle_dataset} -p {download_dir} --unzip"
    
    try:
        subprocess.run(command, shell=True, check=True)
        print(f"Dataset downloaded and saved in: {download_dir}")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while downloading dataset: {e}")
        raise

def extract_zip_files(directory: str):
    for file_name in os.listdir(directory):
        if file_name.endswith(".zip"):
            file_path = os.path.join(directory, file_name)
            print(f"Extracting {file_path}...")
            with ZipFile(file_path, "r") as zip_ref:
                zip_ref.extractall(directory)
            os.remove(file_path)
            print(f"Extracted and removed: {file_path}")

def data_inge(ingestion_config):
    kaggle_dataset = ingestion_config.kaggle_url
    raw_data_dir = ingestion_config.data_dir

    # Download the dataset
    download_dataset(kaggle_dataset, raw_data_dir)
    
    # Extract any zip files
    extract_zip_files(raw_data_dir)
    
    print("Data ingestion complete!")

