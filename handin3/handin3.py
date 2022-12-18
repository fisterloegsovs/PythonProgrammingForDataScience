def read_word_file(filename):
    # Hehe
    tempList = []
    with open(filename, "r") as f:
        for lineNum, line in enumerate(f):
            line = line.strip('\n')
            tempList.append((lineNum, line))
    return tempList

def read_word_file2(filename, word_stem=""):
    tempList = []
    with open(filename, "r") as f:
        for lineNum, line in enumerate(f):
            line = line.strip("\n")
            if word_stem in line:
                tempList.append((lineNum, line))
    return tempList

