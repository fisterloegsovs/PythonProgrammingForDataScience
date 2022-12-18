f = open("Land_and_Ocean_summary.txt","r")
list_of_lines = f.readlines()

for i in range(len(list_of_lines)):
    tempList = list_of_lines[i].split()
    if (len(tempList) > 0) and (tempList[0] != '%') and (int(tempList[0]) >= 2000):
        print(list_of_lines[i], end="")


