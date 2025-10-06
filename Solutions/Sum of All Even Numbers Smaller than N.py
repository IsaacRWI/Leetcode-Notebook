def sumEvenNumbers(n):
    total = 0  # total sum
    while n > 2:  # whilst n is larger than 2 the loop will continue  no point in adding 0 to the total
        if n % 2 == 0:  # if n is an even number
            total += n-2  # add next smaller even number to total sum
            n = n-2  # set n to be next smaller even number
        else:  # else if n is an odd number
            total += n-1  # add next smaller even number
            n = n-1  # set n to be next smaller even number
        sumEvenNumbers(n)  # recursively call function on new n
    return total  # return total sum after the loop breaks

print(sumEvenNumbers(9))