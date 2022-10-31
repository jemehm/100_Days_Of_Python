# posion 1=[0]
# posion 2=[1]
# posion 3=[2]  # posion 1=[1] posion 2=[2] posion 3=[3] posion 4=[4] posion 5=[5] posion 6=[6] posion 7=[7] posion 8=[8] posion 9=[9] posion 10=[10] posion
# start last posion [-1]  
#split string method----------------
import random

names_string = input("Give everybody's names, separated by a comma.")
names= names_string.split(", ")

num_item=len(names)
radom_choice=random.randint(0, num_item-1)
the_person_how_will_pay=names[radom_choice]
print(the_person_how_will_pay +" is going to pay ")