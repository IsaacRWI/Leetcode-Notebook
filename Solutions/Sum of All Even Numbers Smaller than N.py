def sumEvenNumbers(n):
    total = 0
    while n > 2:
        if n % 2 == 0:
            total += n-2
            n = n-2
        else:
            total += n-1
            n = n-1
        sumEvenNumbers(n)
    return total

print(sumEvenNumbers(9))