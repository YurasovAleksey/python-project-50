import pytest
from gendiff import generate_diff

@pytest.fixture
def file1():
    return 'tests/fixtures/file1.json'

@pytest.fixture
def file2():
    return 'tests/fixtures/file2.json'

def test_flat_json_diff(file1, file2):
    expected = """{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}"""
    assert generate_diff(file1, file2) == expected
