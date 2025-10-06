from collections import defaultdict

def groupAnagrams(strs):
    anagram_dict = defaultdict(list)  # default dict creates a key:value element automatically when adding to a non-existent key
    for i in strs:  # for words in strs
        count = [0] * 26  # initialise a list of 26 numbers to count the numbers of letters in the word, a would be index 1 so on
        for j in i:  # for letter in word
            count[ord(j) - ord("a")] += 1  # the index for the letter according to ascii table would + 1,  the ord(j) - ord("a") thing is to set the indexes to start from 0,  as the ascii code for "a" is 97 and 97-97 would be 0 allowing for value setting for count[0].  b would be 98-97=1 count[1]
        key = tuple(count)  # turns the list into a tuple so it can act as the key in the anagram dictionary  as lists are mutable they cannot be hashed and turned into keys
        anagram_dict[key].append(i)  # adds the word to the count key with the corresponding letters,  creates a new key value pair if key is not already in the dictionary
    return list(anagram_dict.values())  # returns only the list of lists of words that are anagrams as per the question

print(groupAnagrams(["ate", "tea", "bat", "tab", "nat"]))