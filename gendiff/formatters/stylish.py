def format(diff, indent=0):
    INDNT = indent + 4
    lines = ['{']
    spaces = ' ' * INDNT

    for key, node in sorted(diff.items()):
        prefix = {
            'added': '+',
            'removed': '-',
            'unchanged': ' ',
            'nested': ' ',
            'changed': ' '
        }[node['type']]

        if node['type'] == 'nested':
            value = format(node['children'], INDNT)
            lines.append(f'{spaces[2:]}{prefix} {key}: {value}')
        elif node['type'] == 'changed':
            lines.append(
                f'{spaces[2:]}- {key}: {to_string(node['old_value'], INDNT)}'
            )
            lines.append(
                f'{spaces[2:]}+ {key}: {to_string(node['new_value'], INDNT)}'
            )
        else:
            lines.append(
                f'{spaces[2:]}{prefix} {key}: {to_string(node['value'], INDNT)}'
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
