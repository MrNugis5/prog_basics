"""File operations."""
import csv


def read_file_contents(filename: str) -> str:
    """
    Read file contents into string.

    In this exercise, we can assume the file exists.

    :param filename: File to read.
    :return: File contents as string.
    """
    with open(filename, "r") as f:
        return f.read()


def read_file_contents_to_list(filename: str) -> list:
    r"""
    Read file contents into list of lines.

    In this exercise, we can assume the file exists.
    Each line from the file should be a separate element.
    The order of the list should be the same as in the file.

    List elements should not contain new line (\n).

    :param filename: File to read.
    :return: List of lines.
    """
    with open(filename, "r") as f:
        lines = [line.rstrip("\n") for line in f]
    return lines


def read_csv_file(filename: str) -> list:
    """
    Read CSV file into list of rows.

    Each row is also a list of "columns" or fields.

    CSV (Comma-separated values) example:
    name,age
    john,12
    mary,14

    Should become:
    [
      ["name", "age"],
      ["john", "12"],
      ["mary", "14"]
    ]

    Use csv module.

    :param filename: File to read.
    :return: List of lists.
    """
    rows = []
    with open(filename) as csv_f:
        csv_reader1 = csv.reader(csv_f, delimiter=",")
        for row in csv_reader1:
            rows.append(row)
    return rows


def write_contents_to_file(filename: str, contents: str) -> None:
    """
    Write contents to file.

    If the file does not exists, create it.

    :param filename: File to write to.
    :param contents: Content to write to.
    :return: None
    """
    f = open(filename, "w")
    f.write(contents)
    f.close()
    return f


def write_lines_to_file(filename: str, lines: list) -> None:
    """
    Write lines to file.

    Lines is a list of strings, each represents a separate line in the file.

    There should be no new line in the end of the file.
    Unless the last element itself ends with the new line.

    :param filename: File to write to.
    :param lines: List of string to write to the file.
    :return: None
    """
    str_lines = ""
    f = open(filename, "w")
    for i in range(len(lines)):
        if i != len(lines) - 1:
            str_lines += lines[i] + "\n"
        else:
            str_lines += lines[i]
    f.write(str_lines)
    f.close


def write_csv_file(filename: str, data: list) -> None:
    """
    Write data into CSV file.

    Data is a list of lists.
    List represents lines.
    Each element (which is list itself) represents columns in a line.

    [["name", "age"], ["john", "11"], ["mary", "15"]]
    Will result in csv file:

    name,age
    john,11
    mary,15

    Use csv module here.

    :param filename: Name of the file.
    :param data: List of lists to write to the file.
    :return: None
    """
    with open(filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=",")
        csv_writer.writerows(data)
    csv_file.close()


def merge_dates_and_towns_into_csv(dates_filename: str, towns_filename: str, csv_output_filename: str) -> None:
    """
    Merge information from two files into one CSV file.

    Dates file contains names and dates. Separated by colon.
    john:01.01.2001
    mary:06.03.2016

    You don't have to validate the date.
    Every line contains name, colon and date.

    Towns file contains names and towns. Separated by colon.
    john:london
    mary:new york

    Every line contains name, colon and town name.
    There are no headers in the input files.

    Those two files should be merged by names.
    The result should be a csv file:

    name,town,date
    john,london,01.01.2001
    mary,new york,06.03.2016

    Applies for the third part:
    If information about a person is missing, it should be "-" in the output file.

    The order of the lines should follow the order in dates input file.
    Names which are missing in dates input file, will follow the order
    in towns input file.
    The order of the fields is: name,town,date

    name,town,date
    john,-,01.01.2001
    mary,new york,-

    Hint: try to reuse csv reading and writing functions.
    When reading csv, delimiter can be specified.

    :param dates_filename: Input file with names and dates.
    :param towns_filename: Input file with names and towns.
    :param csv_output_filename: Output CSV-file with names, towns and dates.
    :return: None
    """
    with open(dates_filename, encoding="utf-8") as f:
        dates = {}
        dates_order = []
        for line in f:
            name, date = line.strip().split(":")
            dates[name] = date
            dates_order.append(name)

    # Step 2: Read the towns file
    with open(towns_filename, encoding="utf-8") as f:
        towns = {}
        towns_order = []
        for line in f:
            name, town = line.strip().split(":")
            towns[name] = town
            towns_order.append(name)

    # Step 3: Merge names in the right order
    all_names = dates_order + [n for n in towns_order if n not in dates]

    # Step 4: Write everything into a CSV file
    with open(csv_output_filename, "w", newline="", encoding="utf-8") as csv_out:
        writer = csv.writer(csv_out)
        writer.writerow(["name", "town", "date"])  # header

        for name in all_names:
            town = towns.get(name, "-")
            date = dates.get(name, "-")
            writer.writerow([name, town, date])
