#Write a program to calculate salary of an employee given his basic pay(to be entered by the user), HRA = 10% of basic pay, TA = 5% ofbasic pay. Define HRA and TA as constants and use them to calculatethe salary of the employee.
import constant
basic = float(input("enter your basic pay"))
salary  = basic + basic*constant.HRA + basic*constant.TA
print(salary)
