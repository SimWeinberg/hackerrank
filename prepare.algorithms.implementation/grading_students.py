# HackerLand University has the following grading policy:

# Every student receives a  in the inclusive range from  to .
# Any  less than  is a failing grade.
# Sam is a professor at the university and likes to round each student's  according to these rules:

# If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
# If the value of  is less than , no rounding occurs as the result will still be a failing grade.

# Given the initial value of  for each of Sam's  students, write code to automate the rounding process.

def gradingStudents(grades):
    newGrades = []
    for i in grades:
        n = i
        while i%5 != 0:
            i += 1
        if n <= 37:
            newGrades.append(n)
        elif i - n < 3:
            newGrades.append(i)
        elif i - n >= 3:
            newGrades.append(n)
    
    return(newGrades)

print(gradingStudents([73,67,38,33]))