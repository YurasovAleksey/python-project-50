import json
from pathlib import Path


def load_file(file_path):
    try:
        path = Path(file_path).resolve()
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f'Invalid JSON: {e}')
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {file_path}')


if __name__ == '__main__':
    file1 = './tests/fixtures/file1.json'
    data = load_file(file1)
    print('Success:', data)
