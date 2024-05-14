def cnt(number):
    if number<10:
        return 1
    else:
        return 1+cnt(number//10)
print(cnt(585))