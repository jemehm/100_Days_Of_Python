student_scores= input("input a list of students scores: ").split()
for n in range(len(student_scores)) :
    student_scores[n] =int(student_scores[n])
print(student_scores)
high_score = 0
for scores in student_scores:
    if scores > high_score:
        high_score = scores
print(f"The highest score in the class is {high_score}") 

