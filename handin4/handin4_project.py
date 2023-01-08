def read_data4(filename, year_range=None, decade=False):
    with open(filename, "r") as f:
        data = f.readlines()
    data = [line.strip() for line in data]
    decade_dict = {}
    if year_range:
        start, end = year_range
    else:
        start = None
        end = None
    for line in data:
        if not line[:4].isdigit():
            continue
        year = int(line[:4])
        if start and end and (year < start or year > end):
            continue
        values = list(map(float, line[5:].split()))
        if decade:
            if year % 10 == 0:
                decade_dict[year] = values
        else:
            decade_dict[year] = values
    return decade_dict
