l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
if (r1 >= l2 and r2 >= l3 and r3 >= l2) or (r2 >= l3 and r3 >= l1 and r1 >= l3) or (r3 >= l1 and r1 >= l2 and r2 >= l1):
    print(0) #допустим здесь все хорошо
else:
