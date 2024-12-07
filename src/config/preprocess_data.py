import yaml
from utils.common import read_yaml

params=read_yaml("config.yaml")

class preprocess_config:
  def __init__(self):
    self.raw_data_dir=params["preprocess_data"]["raw_dir"]
    self.processed_data_dir=params["preprocess_data"]["prprocessed_dir"]
    self.model_dir=params["preprocess_data"]["model_dir"]