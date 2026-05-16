import os
import yaml
from pathlib import Path
from dotenv import load_dotenv

class Config:
    def __init__(self, env: str = None):
        # Load environment variables from .env file
        load_dotenv()
        self.env = env or os.getenv('ENV', 'staging')
        self.base_url = None
        self.api_url = None
        self.browser = None
        self.headless = None
        self.slow_mo = None
        self.timeout = None
        self.api_timeout = None
        self.screenshot_on_failure = None
        self._load()


    def _load(self):
        config_path = Path(__file__).parent / 'config.yaml'
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)

        env_config = config["environments"][self.env]
        required_keys = ["base_url", "api_base_url"]
        for key in required_keys:
            if key not in env_config:
                raise KeyError(
                    f"Missing required config key '{key}' "
                    f"for environment '{self.env}' in config.yaml"
                )
        self.base_url = env_config["base_url"]
        self.api_url = env_config["api_base_url"]
        self.browser = config["browser"]["name"]
        self.headless = os.getenv('HEADLESS', str(config["browser"]["headless"])).lower() == 'true'
        self.timeout = config["browser"]["timeout"]
        self.slow_mo = config["browser"]["slow_mo"]
        self.api_timeout = config["api"]["timeout"]
        self.screenshot_on_failure = config["reporting"]["screenshot_on_failure"]
    
_config = None

def get_config()-> Config:
    global _config
    if _config is None:
        _config = Config()
    return _config