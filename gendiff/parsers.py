import json
from pathlib import Path

import yaml


def parse_file(file_path):
    path = Path(file_path)
    content = path.read_text()

    if path.suffix == '.json':
        return parse_json(content)
    elif path.suffix in ('.yaml', '.yml'):
        return parse_yaml(content)
    raise ValueError(f'Unsupported format: {path.suffix}')


def parse_json(content):
    try:
        return json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f'Invalid JSON: {e}')


def parse_yaml(content):
    try:
        return yaml.safe_load(content)
    except yaml.YAMLError as e:
        raise ValueError(f'Invalid YAML: {e}')
