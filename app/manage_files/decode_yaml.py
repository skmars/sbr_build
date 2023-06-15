import yaml


def get_yaml_data(file_dir: str):
    try:
        with open(file_dir) as f:
            yaml_data = yaml.safe_load(f)
        return yaml_data
    except Exception as ex:
        raise ValueError(f"It's imposible to decode {file_dir}. {ex}")
