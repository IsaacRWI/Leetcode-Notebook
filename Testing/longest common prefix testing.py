str = "elephant"

print(len(str))

list = ["monk", "cheese"]

for i in range(len(list[0])):  # for the number of letters in list[0]
#    print(i)
    for s in list:  # for every word in list
        print(s[i])  # print a letter of the word for the index rn

for i in range(2):
    print("2")