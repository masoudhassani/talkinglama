import yaml
import os
import sys

pwd = os.path.dirname(__file__)
sys.path.append(pwd)


def load_configs(path):
    try:
        with open(os.path.join(pwd, path), "r") as f:
            configs = yaml.load(f, Loader=yaml.SafeLoader)

        return configs

    except:
        print(f"file not found: {os.path.join(pwd, path)}")
        return None
