


print("Wellcome to the rollercoaster!!")
height= int(input("What is your height in cm?"))
age= int(input("how old are you?"))
bill=0
photo = 3

if height >=120:
    if age <= 49:
        bill=8
        print("it cost 8$")
    elif age<= 12:
        bill= 5
        print("it cost 5$")
       
    elif age >= 50:
        bill= 0
        print(f"you can ride for Free!")
    if height >=120:
        Y=input("do you want photo? Y/N")
    if Y :
        print(bill+3)
 


    
    #print("you can ride") 
else:
    print("sorry, you can't ride")
