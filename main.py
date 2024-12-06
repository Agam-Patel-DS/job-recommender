# Entry point for the Job Recommender System
from src.config.data_ingestion import data_ingestion
from src.data_processing.data_ingestion import data_inge

data_config=data_ingestion()
data_inge(data_config)