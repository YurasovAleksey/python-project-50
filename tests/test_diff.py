import pytest
import os
from gendiff import generate_diff

def get_fixture_path(file_name):
    return os.path.join('tests', 'fixtures', file_name)

TEST_CASES = [
    ('file1.json', 'file2.json', 'expected_json.txt'),
    ('file1.yaml', 'file2.yaml', 'expected_yaml.txt')
]

@pytest.mark.parametrize('file1, file2, expected', TEST_CASES)
def test_diff(file1, file2, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)

    with open(expected_path) as f:
        expected_result = f.read().strip()
    
    assert generate_diff(file1_path, file2_path) == expected_result
