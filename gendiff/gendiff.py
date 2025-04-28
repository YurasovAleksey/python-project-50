import json
from pathlib import Path


def load_file(file_path):
    try:
        path = Path(file_path)
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f'Invalid JSON: {e}')
    except FileNotFoundError:
        raise FileNotFoundError(f'File not found: {file_path}')


def generate_diff(file_path1, file_path2):
    data1 = load_file(file_path1)
    data2 = load_file(file_path2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff_lines = []

    for key in all_keys:
        if key not in data2:
            diff_lines.append(f'  - {key}: {data1[key]}')
        elif key not in data1:
            diff_lines.append(f'  + {key}: {data2[key]}')
        elif data1[key] != data2[key]:
            diff_lines.append(f'  - {key}: {data1[key]}')
            diff_lines.append(f'  + {key}: {data2[key]}')
        else:
            diff_lines.append(f'    {key}: {data1[key]}')

    return '{\n' + '\n'.join(diff_lines) + '\n}'


if __name__ == '__main__':
    file1 = './tests/fixtures/file1.json'
    file2 = './tests/fixtures/file2.json'
    diff = generate_diff(file1, file2)
    print(diff)
