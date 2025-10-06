class Solution:
    def encode(self, strs):
        res = ""  # output string
        for i in strs:  # for item in list
            res += str(len(i)) + "#" + i  # appends length of item, a delimiter then the item in string form into the output string
        return res

    def decode(self, str):
        res = []  # output list
        counter = 0  # counter for the letter of the string we're on rn

        while counter < len(str):  # whilst we're still in bounds
            ccount = counter  # character count (for the word we're on rn) is set to the index we're on for the main counter
            while str[ccount] != "#":  # whilst the character in the string is not our delimiter
                ccount += 1  # character in the word += 1
            # ccount basically counts the number of numbers before the delimiter and hence gives us the number of digits we have
            # the difference between the main counter and ccount is the number of digits for the number dictating how long the next word will be

            word_length = int(str[counter:ccount])  # after finding our delimiter and breaking out of the loop, sets word length to the length of the word (the letter before the delimiter and the word)
            res.append(str[ccount + 1: ccount + 1 + word_length])  # appends the characters after the delimiter for the length of the word as an item to the output list
            counter = ccount + 1 + word_length  # sets counter to start of next word  ie the beginning with the integer for the number of characters in the next word
        return res

test1 = Solution
test1_encoded = test1.encode(0,["hello", "bye#", "##heu"])
print(test1_encoded)
print(test1.decode(0, test1_encoded))