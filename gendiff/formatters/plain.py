def format(diff):
    def walk(node, path):
        lines = []
        for key, val in sorted(node.items()):
            current_path = f'{path}.{key}' if path else key
            if val['type'] == 'nested':
                lines.extend(walk(val['children'], current_path))
            elif val['type'] == 'changed':
                lines.append(
                    f"Property '{current_path}' was updated. "
                    f"From {format_value(val['old_value'])} "
                    f"to {format_value(val['new_value'])}"
                )
            elif val['type'] == 'added':
                lines.append(
                    f"Property '{current_path}' was added "
                    f"with value: {format_value(val['value'])}"
                )
            elif val['type'] == 'removed':
                lines.append(f"Property '{current_path}' was removed")
        return lines
    
    return '\n'.join(walk(diff, ''))


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    return str(value)
