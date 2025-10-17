# apparently there are no years between 1987 and 2013 that have no repeating digits in the year

def noRepeats(year):
    counter = 1987
    while counter < year:
        print(counter)
        counter += 1
        counter_list = [int(i) for i in str(counter)]
        counter_set = set(counter_list)
        if len(counter_set) == len(counter_list):
            print("no repeats", counter)
            return
    print("no non-repeats")
print(noRepeats(2012))