import pytest
import os
from gendiff import generate_diff


PATH_JSON1 = 'flat/file1.json'
PATH_JSON2 = 'flat/file2.json'
PATH_YML1 = 'flat/file1.yaml'
PATH_YML2 = 'flat/file2.yaml'

PTH_TREE_JSON1 = 'nested/file_tree1.json'
PTH_TREE_JSON2 = 'nested/file_tree2.json'
PTH_TREE_YML1 = 'nested/file_tree1.yaml'
PTH_TREE_YML2 = 'nested/file_tree2.yaml'

TEST_CASES = [
    (PATH_JSON1, PATH_JSON2, 'stylish', 'flat/expected.txt'),
    (PATH_YML1, PATH_YML2, 'stylish', 'flat/expected.txt'),
    (PATH_JSON1, PATH_JSON2, 'plain', 'flat/expected_plain.txt'),
    (PATH_YML1, PATH_YML2, 'plain', 'flat/expected_plain.txt'),
    (PATH_JSON1, PATH_JSON2, 'json', 'flat/expected.json'),
    (PATH_YML1, PATH_YML2, 'json', 'flat/expected.json'),
    (PTH_TREE_JSON1, PTH_TREE_JSON2, 'stylish', 'nested/expected.txt'),
    (PTH_TREE_YML1, PTH_TREE_YML2, 'stylish', 'nested/expected.txt'),
    (PTH_TREE_JSON1, PTH_TREE_JSON2, 'plain', 'nested/expected_plain.txt'),
    (PTH_TREE_YML1, PTH_TREE_YML2, 'plain', 'nested/expected_plain.txt'),
    (PTH_TREE_JSON1, PTH_TREE_JSON2, 'json', 'nested/expected.json'),
    (PTH_TREE_YML1, PTH_TREE_YML2, 'json', 'nested/expected.json')
]


def get_fixture_path(*args):
    return os.path.join('tests', 'fixtures', *args)


@pytest.mark.parametrize('file1, file2, format_name, expected', TEST_CASES)
def test_diff(file1, file2, format_name, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)

    with open(expected_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(file1_path, file2_path, format_name) == expected_result
