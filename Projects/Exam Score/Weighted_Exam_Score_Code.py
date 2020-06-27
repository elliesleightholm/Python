"""
Created on Wed Mar 11 20:57:55 2020

@author: elliesleightholm
"""

# Weighted Exam Score Average 

num =int(input("Enter number of exams : "))  # Enter how many exams you've done
average = 0
year = int(input("Enter how many credits these exams cover : ")) # Enter the total number of credits these exams cover
for i in range(num):
    score = int(input("Enter Exam Score : ")) # Here you enter your exam score 
    credit = int(input("Enter how many credits is this exam worth : ")) # and the amount of credits it was worth
    average = average + score*credit/year
print("Your average is", average)
