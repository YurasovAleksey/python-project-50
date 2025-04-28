from gendiff.parsers import parse_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)
    return format_diff(diff, format_name)


def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    result = {}

    for key in all_keys:
        if key not in data2:
            result[key] = {'type': 'removed', 'value': data1[key]}
        elif key not in data1:
            result[key] = {'type': 'added', 'value': data2[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {
                'type': 'nested',
                'children': build_diff(data1[key], data2[key])
            }
        elif data1[key] != data2[key]:
            result[key] = {
                'type': 'changed',
                'old_value': data1[key],
                'new_value': data2[key]
            }
        else:
            result[key] = {'type': 'unchanged', 'value': data1[key]}

    return result


def format_diff(diff, format_name):
    from gendiff.formatters import stylish
    return stylish.format(diff)
