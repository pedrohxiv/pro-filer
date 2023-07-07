from pro_filer.actions.main_actions import show_details  # NOQA
from datetime import date


def test_show_details_file_not_exists(capsys):
    context = {
        "base_path": "/????"
    }

    show_details(context)

    captured = capsys.readouterr()
    expected_output = "File '????' does not exist\n"
    assert captured.out == expected_output


def test_show_details_file_exists_without_extension(capsys, tmp_path):
    file = tmp_path / "pro-filer-preview"
    file.touch()

    context = {
        "base_path": str(file)
    }

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        "File name: pro-filer-preview\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        f"Last modified date: {date.today()}\n"
    )
    assert captured.out == expected_output


def test_show_details_file_exists_with_extension(capsys, tmp_path):
    file = tmp_path / "pro-filer-preview.gif"
    file.touch()

    context = {
        "base_path": str(file)
    }

    show_details(context)

    captured = capsys.readouterr()
    expected_output = (
        "File name: pro-filer-preview.gif\n"
        "File size in bytes: 0\n"
        "File type: file\n"
        "File extension: .gif\n"
        f"Last modified date: {date.today()}\n"
    )
    assert captured.out == expected_output
