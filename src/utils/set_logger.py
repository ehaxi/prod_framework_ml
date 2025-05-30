import logging.config
import yaml
from datetime import datetime

def setup_logging(project_root, root_file):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"{project_root}/logs/{root_file}_{timestamp}.log"

    with open(f"{project_root}/config/logging.yaml", "r") as f:
        config = yaml.safe_load(f)

    config['handlers']['file']['filename'] = log_filename

    logging.config.dictConfig(config)