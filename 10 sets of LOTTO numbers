from random import randrange

# 10 εξαδες ΛΟΤΤΟ, οπου
# 1) Δυο αριθμοι θα ειναι στο ευρος 10 εως 19
# 2) Δυο αριθμοι θα ειναι στο ευρος 20 εως 39
# 3) Ενας αριθμος θα ειναι ζυγος στο ευρος 1 εως 9
# 4) Ενας αριθμος θα ειναι μονος στο ευρος 40 εως 49

A = set()
lotto_tuple = ()
for i in range(10):
    a = randrange(1, 10)
    while a % 2 == 0:
        a = randrange(1, 10)
    d = randrange(40, 50)
    while d % 2 != 0:
        d = randrange(40, 50)
    b1 = randrange(10, 20)
    b2 = randrange(10, 20)
    while b1 == b2:
        b2 = randrange(10, 20)
    c1 = randrange(20, 40)
    c2 = randrange(20, 40)
    while c1 == c2:
        c2 = randrange(20, 40)
    lotto_tuple = (a, b1, b2, c1, c2, d)
    A.add(lotto_tuple)
for ele in A:
    print(ele, end=" ")
    print(" ")
