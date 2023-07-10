import pytest

from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_find_duplicate_files_empty(tmp_path):
    file1 = tmp_path / "file1.txt"
    file2 = tmp_path / "file2.txt"
    file3 = tmp_path / "file3.txt"

    context = {
         "all_files": [str(file1), str(file2), str(file3)]
    }

    with pytest.raises(ValueError):
        find_duplicate_files(context)


def test_find_duplicate_files_no_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text('Lorem ipsum dolor sit amet, consectetur adipiscing.')
    file2 = tmp_path / "file2.txt"
    file2.write_text('Nulla facilisi.')
    file3 = tmp_path / "file3.txt"
    file3.write_text('Sed ut libero eget diam malesuada euismod.')

    context = {
        "all_files": [str(file1), str(file2), str(file3)]
    }

    assert len(find_duplicate_files(context)) == 0


def test_find_duplicate_files_duplicates(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text('Lorem ipsum dolor sit amet, consectetur adipiscing.')
    file2 = tmp_path / "file2.txt"
    file2.write_text('Nulla facilisi.')
    file3 = tmp_path / "file3.txt"
    file3.write_text('Lorem ipsum dolor sit amet, consectetur adipiscing.')

    context = {
        "all_files": [str(file1), str(file2), str(file3)]
    }

    assert len(find_duplicate_files(context)) == 1
