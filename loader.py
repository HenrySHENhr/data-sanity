import csv
import io
import os


def load_csv_file(csv_file):
    """
    Load csv file

    :param csv_file: csv file path
    :return: list of parameters

    Examples:
        >>> cat csv_file
        username,password
        test1,111111
        test2,222222
        test3,333333

        >>> load_csv_file(csv_file)
        [
            {'username': 'test1', 'password': '111111'},
            {'username': 'test2', 'password': '222222'},
            {'username': 'test3', 'password': '333333'}
        ]

    """
    if not os.path.isabs(csv_file):
        project_working_directory = os.getcwd()
        csv_file = os.path.join(project_working_directory, *csv_file.split("/"))

    if not os.path.isfile(csv_file):
        raise FileNotFoundError

    csv_content_list = []

    with io.open(csv_file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            csv_content_list.append(row)

    return csv_content_list
