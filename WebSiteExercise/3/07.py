bet, res = int(input()), int(input())

if bet in range(13) and res == bet:
        print(120)

elif bet == 13 and not(res%2):
        print(20)

elif bet == 14 and res%2:
        print(20)

elif bet == 15 and res in [1,3,5,7,9,12]:
        print(20)

elif bet == 16 and res in [2,4,6,8,10,11]:
    print(20)

else:
    print(0)