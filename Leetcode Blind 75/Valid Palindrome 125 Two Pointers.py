def isPalindrome(s):
    string = ""
    for i in s:
        if i.isalnum():  # checks if i is a letter or number
            string += i.lower()
    if string == string[::-1]:
        return True
    else:
        return False

print(isPalindrome("racecar"))
print(isPalindrome("cheese"))