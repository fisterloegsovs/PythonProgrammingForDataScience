def wordfile_to_list(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

def wordfile_to_dict(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
        return {line.strip(): None for line in lines}
    
def wordfile_to_set(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    return set(line.strip() for line in lines) 

def wordfile_differences_list_search(file1, file2):
    wordList1 = wordfile_to_list(file1)
    wordList2 = wordfile_to_list(file2)
    differences = []
    for word in wordList1:
        if word not in wordList2:
            differences.append(word)
    return differences

def wordfile_differences_dict_search(file1, file2):
    wordList = wordfile_to_list(file1)
    wordDict = wordfile_to_dict(file2)
    differences = []
    for word in wordList:
        if word not in wordDict.keys():
            differences.append(word)
    return differences

def wordfile_differences_set_search(file1, file2):
    set1 = wordfile_to_set(file1)
    set2 = wordfile_to_set(file2)
    return list(set1 - set2)