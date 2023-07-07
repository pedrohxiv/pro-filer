from pro_filer.actions.main_actions import show_disk_usage  # NOQA


def test_show_disk_usage_empty_files(capsys):
    context = {
        "all_files": []
    }

    show_disk_usage(context)

    captured = capsys.readouterr()
    assert 'Total size: 0' in captured.out


def test_show_disk_usage_single_file(capsys, tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text('Lorem ipsum dolor sit amet, consectetur adipiscing.')

    context = {
        "all_files": [str(file1)]
    }

    show_disk_usage(context)

    captured = capsys.readouterr()
    assert 'file1.txt' in captured.out
    assert '51 (100%)' in captured.out
    assert 'Total size: 51' in captured.out


def test_show_disk_usage_multiple_files(capsys, tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text('Lorem ipsum dolor sit amet, consectetur adipiscing.')
    file2 = tmp_path / "file2.txt"
    file2.write_text('Nulla facilisi.')

    context = {
        "all_files": [str(file1), str(file2)]
    }

    show_disk_usage(context)

    captured = capsys.readouterr()
    assert captured.out.index("file1.txt") < captured.out.index("file2.txt")
