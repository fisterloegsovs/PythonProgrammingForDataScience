with open("Land_and_Ocean_summary.txt", "r") as f:
    data_list = [i for i in filter(lambda i: i.strip(), f) if not i.startswith("%")]


def read_data(filename):
    with open(filename, "r") as f:
      data_list = [i for i in filter(lambda i: i.strip(), f) if not i.startswith("%")]
    return data_list

def read_data2(filename, year_range=None):
    with open(filename, "r") as f:
        data_list = [i for i in filter(lambda i: i.strip(), f) if not i.startswith("%") and (year_range is None or int(i.split()[0]) in range(*year_range))]
    return data_list
