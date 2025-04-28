import pytest
import os
from gendiff import generate_diff

def get_fixture_path(*args):
    return os.path.join('tests', 'fixtures', *args)

TEST_CASES = [
    ('flat/file1.json', 'flat/file2.json', 'flat/expected.txt'),
    ('flat/file1.yaml', 'flat/file2.yaml', 'flat/expected.txt'),
    ('nested/file_tree1.json', 'nested/file_tree2.json', 'nested/expected.txt'),
    ('nested/file_tree1.yaml', 'nested/file_tree2.yaml', 'nested/expected.txt')
]

@pytest.mark.parametrize('file1, file2, expected', TEST_CASES)
def test_diff(file1, file2, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)

    with open(expected_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(file1_path, file2_path) == expected_result
