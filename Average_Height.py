from itertools import count
from operator import index


studint_height = input("Input a list of studint heights: ").split()
for n in range(0, len(studint_height)):
    studint_height[n] = int(studint_height[n])
total_height= 0
for height in studint_height:
    total_height += height
number_of_studint =0
for studint in studint_height:
    number_of_studint += 1    

average_height = round(total_height/number_of_studint)
print(number_of_studint)    
print(total_height)
print(average_height)