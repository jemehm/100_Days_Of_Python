import random

for r in range(14):
    i= range(1, 37)
    lotto= [random.randrange(1,37,1) for i in range(6)]
    lotto = sorted(set(lotto))


    strong= [random.randrange(1,7,1) for num in range(1)] 
    extra= [random.randrange(1,7,1) for num in range(7)] 

    print(f"{r+1} :{lotto}, strong: {strong}")
print(extra)

