import json


def format(diff):
    def process_node(node):
        if not isinstance(node, dict):
            return node

        if 'type' in node:
            return node

        result = {}
        for key, value in node.items():
            if not isinstance(value, dict):
                result[key] = value
                continue

            node_type = value.get('type')
            
            if node_type == 'nested':
                result[key] = {
                    'type': 'nested',
                    'value': process_node(value['children'])
                }
            elif node_type == 'changed':
                result[key] = {
                    'type': 'changed',
                    'old_value': process_node(value['old_value']),
                    'new_value': process_node(value['new_value'])
                }
            elif node_type in ('added', 'removed', 'unchanged'):
                result[key] = {
                    'type': node_type,
                    'value': process_node(value['value'])
                }
            else:
                result[key] = value 
        return result

    return json.dumps(process_node(diff), indent=2, ensure_ascii=False)
# def format(diff):
#     def process_node(node):
#         if not isinstance(node, dict):
#             return node
    
#         if 'type' in node:
#             return node
        

#         result = {}
#         for key, value in node.items():
#             node_type = value['type']

#             if node_type == 'nested':
#                 result[key] = {
#                     'type': 'nested',
#                     'value': process_node(value['children'])
#                 }
#             elif node_type == 'changed':
#                 result[key] = {
#                     'type': 'changed',
#                     'old_value': process_node(value['old_value']),
#                     'new_value': process_node(value['new_value'])
#                 }
#             else:
#                 result[key] = {
#                     'type': node_type,
#                     'value': process_node(value['value'])
#                 }
#         return result

#     return json.dumps(process_node(diff), indent=2, ensure_ascii=False)
