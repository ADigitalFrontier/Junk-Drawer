def summation(start, end, func):
    total = 0
    for i in range(start, end + 1):
        total += func(i)
    return total


inner_sum = lambda n : ((11-n)*(1)+(n-1)*(100))/9


print(summation(1, 10, lambda i : ((i/55)*(summation(1, i-1, inner_sum) + summation(i+1, 10, inner_sum)))))