def format(diff, indent=0):
    lines = ['{']
    spaces = ' ' * (indent + 4)

    for key, node in sorted(diff.items()):
        prefix = {
            'added': '+',
            'removed': '-',
            'unchanged': ' ',
            'nested': ' ',
            'changed': ' '
        }[node['type']]

        if node['type'] == 'nested':
            value = format(node['children'], indent + 4)
            lines.append(f'{spaces[2:]}{prefix} {key}: {value}')
        elif node['type'] == 'changed':
            lines.append(
                f'{spaces[2:]}- {key}: {to_string(node['old_value'], indent + 4)}'
            )
            lines.append(
                f'{spaces[2:]}+ {key}: {to_string(node['new_value'], indent + 4)}'
            )
        else:
            lines.append(
                f'{spaces[2:]}{prefix} {key}: {to_string(node['value'], indent + 4)}'
            )
    lines.append(' ' * indent + '}')
    return '\n'.join(lines)


def to_string(value, current_indent):
    if isinstance(value, dict):
        lines = ['{']
        inner_spaces = ' ' * (current_indent + 4)
        for k, v in sorted(value.items()):
            lines.append(
                f'{inner_spaces}{k}: {to_string(v, current_indent + 4)}'
            )
        lines.append(' ' * current_indent + '}')
        return '\n'.join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)
