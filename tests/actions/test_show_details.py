from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_file_not_exists(capsys):
    context = {
        "base_path": "/home/pedro/trybe-projetos/????"
    }

    show_details(context)

    captured = capsys.readouterr()
    expected_output = "File '????' does not exist\n"
    assert captured.out == expected_output


def test_show_details_file_exists_without_extension(capsys):
    context = {
        "base_path": "/home/pedro/trybe-projetos/" +
        "python-026-python-projeto-pro-filer/images"
    }

    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        "File name: images\n"
        "File size in bytes: 4096\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-07-06\n"
    )
    assert captured.out == expected_output


def test_show_details_file_exists_with_extension(capsys):
    context = {
        "base_path": "/home/pedro/trybe-projetos/" +
        "python-026-python-projeto-pro-filer/images/pro-filer-preview.gif"
    }

    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        "File name: pro-filer-preview.gif\n"
        "File size in bytes: 270824\n"
        "File type: file\n"
        "File extension: .gif\n"
        "Last modified date: 2023-07-06\n"
    )
    assert captured.out == expected_output
