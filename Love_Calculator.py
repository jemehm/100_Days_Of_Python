#Love Calculator



print("Welcome to the Love Calculator!!")
name1 = input("Please enter your name: ")
name2 = input("Please enter your crash name: ")

combined = name1 + name2
lower_case_string = combined.lower()

t= lower_case_string.count("t")
r= lower_case_string.count("r")
u= lower_case_string.count("u")
e= lower_case_string.count("e")

true =t+r+u+e

l= lower_case_string.count("l")
o= lower_case_string.count("o")
v= lower_case_string.count("v")
e= lower_case_string.count("e")

love= l+o+v+e

love_score= str(true)+str(love)

if (love_score < "10") or (love_score > "90"):
    print(f"your love score is {love_score} , you go together like cock& mentos")
elif (love_score >= "40") and (love_score <= "50"):
    print(f"your love score is {love_score}, you are alright together.")
else:
    print(f"your love score is {love_score}.")