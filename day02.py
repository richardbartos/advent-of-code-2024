import os.path

data_input = []
dampened = False


def is_sequence(integer_list):
    tmp_results = []

    for i in range(len(integer_list) - 1):
        if integer_list[i] > integer_list[i + 1]:
            tmp_results.append(True)
        elif integer_list[i] < integer_list[i + 1]:
            tmp_results.append(False)
        else:
            return False

    if all(tmp_results) or not any(tmp_results):
        return True
    else:
        return False


def is_sequence_damp(integer_list):
    tmp_results = []
    global dampened

    for i in range(len(integer_list) - 1):
        if integer_list[i] > integer_list[i + 1]:
            tmp_results.append(True)
        elif integer_list[i] < integer_list[i + 1]:
            tmp_results.append(False)
        else:
            return False

    print(tmp_results)

    if all(tmp_results) or not any(tmp_results):
        return True
    else:
        return False


def is_small_step(integer_list):
    tmp_results = []

    for i in range(len(integer_list) - 1):
        if abs(integer_list[i] - integer_list[i + 1]) <= 3:
            tmp_results.append(True)
        else:
            tmp_results.append(False)

    if all(tmp_results):
        return True
    else:
        return False


def is_small_step_damp(integer_list):
    tmp_results = []

    for i in range(len(integer_list) - 1):
        if abs(integer_list[i] - integer_list[i + 1]) <= 3:
            tmp_results.append(True)
        else:
            tmp_results.append(False)

    if all(tmp_results):
        return True
    else:
        return False


def all_but_one_equal(arr):
    counts = [0] * len(arr)
    unique_elements = []

    for item in arr:
        if item in unique_elements:
            counts[unique_elements.index(item)] += 1
        else:
            unique_elements.append(item)
            counts[unique_elements.index(item)] = 1

    most_common_type = max(counts)

    return most_common_type == len(arr) or most_common_type == len(arr) - 1


def find_safe_reports(data):
    """
    >>> find_safe_reports(["7 6 4 2 1",
    ... "1 2 7 8 9",
    ... "9 7 6 2 1",
    ... "1 3 2 4 5",
    ... "8 6 4 4 1",
    ... "1 3 6 7 9 10 13"])
    2
    """

    count = 0
    edited_data = data

    for item in edited_data:
        substrings = item.split()
        integer_list = [int(num) for num in substrings]

        if is_sequence(integer_list) and is_small_step(integer_list):
            count += 1

    return count


def find_safe_reports_dampened(data):
    """
    >>> find_safe_reports_dampened(["7 6 4 2 1",
    ... "1 2 7 8 9",
    ... "9 7 6 2 1",
    ... "1 3 2 4 5",
    ... "8 6 4 4 1",
    ... "1 3 6 7 9 10 13"])
    4
    """

    count = 0
    edited_data = data

    for item in edited_data:
        substrings = item.split()
        integer_list = [int(num) for num in substrings]

        if is_sequence_damp(integer_list) and is_small_step_damp(integer_list):
            count += 1

    return count


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day02.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Number of safe reports: " + str(find_safe_reports(data_input)))
    print("Number of safe reports with dampener: " + str(find_safe_reports_dampened(data_input)))
