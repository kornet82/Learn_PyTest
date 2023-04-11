import pytest

@pytest.fixture(autouse=True)
def clean_file():
    with open("tests/test_file.txt", "w") as f_o:
        pass