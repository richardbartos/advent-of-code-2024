import os.path

data_input = []


def find_distances(data):
    """
    >>> find_distances(["3   4",
    ... "4   3",
    ... "2   5",
    ... "1   3",
    ... "3   9",
    ... "3   3"])
    11
    """

    distance = 0
    edited_data = data
    first_list = []
    second_list = []

    for item in edited_data:
        first_list.append(item.split()[0])
        second_list.append(item.split()[1])

    first_list.sort()
    second_list.sort()

    for i in range(len(first_list)):
        distance += abs(int(first_list[i])-int(second_list[i]))

    return distance


if __name__ == "__main__":
    with open(os.path.join(os.path.dirname(__file__), 'day01.txt')) as fh:
        for line in fh.readlines():
            line = line.strip()
            data_input.append(line)

    print("Total distances: " + str(find_distances(data_input)))
