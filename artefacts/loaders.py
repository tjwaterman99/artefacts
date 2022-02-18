import json
import os

from .config import Config


class FileSystemLoader:
    def __init__(self, config=Config()):
        self.config = config

    def load(self, artifact_name):
        if not artifact_name.endswith('.json'):
            artifact_name += '.json'
        
        artifact_fp = os.path.join(self.config.dbt_target_dir, artifact_name)

        with open(artifact_fp, 'r') as fh:
            return json.load(fh)
