# Entry point for the Job Recommender System
from src.config.data_ingestion import data_ingestion
from src.data_processing.data_ingestion import data_inge
from src.data_processing.preprocess_data import preprocess
from src.config.preprocess_data import preprocess_config

# data_config=data_ingestion()
# data_inge(data_config)

prep_config=preprocess_config()
preprocess(prep_config)