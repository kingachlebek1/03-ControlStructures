for x in range(1,31):
    if x%3==0 and x%5==0:
        print("bingo")
    elif x%3==0:
        print("THREE")
    elif x%5==0:
        print("Five")
    else:
        print(x)