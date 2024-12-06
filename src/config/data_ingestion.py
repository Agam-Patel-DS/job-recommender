# Data Ingestion Configuration
import yaml
from utils.common import read_yaml

params=read_yaml("config.yaml")

class data_ingestion:
  def __init__(self):
    self.kaggle_url=params["data_ingestion"]["kaggle_url"]
    self.data_dir=params["data_ingestion"]["data_dir"]