def read_data3(filename, year_range=(0, 1000000)):
    # initialise empty dictionary
    data = {}
    # Open file for reading and read and save contents as file
    with open(filename, "r") as file:
        for line in file:
            # Skips comment lines or lines that are empty
            if line.startswith("%") or not line.strip():
                continue
            # split lines into elements
            elements = line.split()
            year = int(elements[0])
            # Add the year and values to the dictionary 
            # if the year is within the specified range
            if year_range[0] <= year < year_range[1]:
                values = [float(value) for value in elements[1:]]
                data[year] = values
    return data