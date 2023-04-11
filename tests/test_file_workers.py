from my_funcs.file_workers import read_from_file


def test_read_from_file():
    test_data = ["one\n", "two\n", "three\n"]
    with open("tests/test_file.txt", "a") as f_o:
        f_o.writelines(test_data)
    assert test_data == read_from_file("tests/test_file.txt")


