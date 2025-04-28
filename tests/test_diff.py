import pytest
import os
from gendiff import generate_diff

def get_fixture_path(*args):
    return os.path.join('tests', 'fixtures', *args)

TEST_CASES = [
    ('flat/file1.json', 'flat/file2.json', 'stylish', 'flat/expected.txt'),
    ('flat/file1.yaml', 'flat/file2.yaml', 'stylish', 'flat/expected.txt'),
    ('flat/file1.json', 'flat/file2.json', 'plain', 'flat/expected_plain.txt'),
    ('flat/file1.yaml', 'flat/file2.yaml', 'plain', 'flat/expected_plain.txt'),
    ('nested/file_tree1.json', 'nested/file_tree2.json', 'stylish', 'nested/expected.txt'),
    ('nested/file_tree1.yaml', 'nested/file_tree2.yaml', 'stylish', 'nested/expected.txt'),
    ('nested/file_tree1.json', 'nested/file_tree2.json', 'plain', 'nested/expected_plain.txt'),
    ('nested/file_tree1.yaml', 'nested/file_tree2.yaml', 'plain', 'nested/expected_plain.txt')
]

@pytest.mark.parametrize('file1, file2, format_name, expected', TEST_CASES)
def test_diff(file1, file2, format_name, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)

    with open(expected_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(file1_path, file2_path, format_name) == expected_result
