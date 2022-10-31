print("welcome to the Tip calculator.")
bill= float(input("What is the total bill? $"))
pirsent= float(input("What is persantage want to give? 10, 12 or more? "))
num= float(input("how many people you are?"))
b= pirsent / 100 * bill +bill 
total = b / num
t=round(total,2)
print(f"every one shuld pay ${t}")