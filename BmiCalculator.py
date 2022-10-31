height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

result= float( weight/ height **2)
res =round(result,2)

if res <= 18.5:
    print("you must eat")
elif (res > 18.5) and (res <   25):
    print(f"{res} your weight is good enough")
elif (res > 25) and (res < 29.9):
    print(f"{res} you must workout")
elif (res > 29.9) and(res< 35):
    print(f"{res} you are fat")

print(res)