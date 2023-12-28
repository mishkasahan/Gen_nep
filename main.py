def nepar(a: int, b: int):
    while True:
        if a > b:
            break
        if a % 2 == 0:
            a += 1
        else:
            yield a
            a +=1

n = nepar(2,7)

for i in n:
    print(i)
