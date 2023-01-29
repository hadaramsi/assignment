def summer(num):
    if num == 0:
        return 0
    return (num % 10) + summer(int(num/10))


res = summer(2347623)
print(res)
