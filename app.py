import addition as ad
import subtraction as sb
import multiplication as mt
import division as dv

print("choices:")
print("1 - add")
print("2 - subtract")
print("3 - multiply")
print("4 - divide")
selection = input("Enter the number of your selection:")
num1 = input("Write the first number ")
num2 = input("Write the second number ")
selection = int(selection)
num1 = int(num1)
num2 = int(num2)


if(selection == 1):
    print(ad.addTwoNums(num1, num2))
elif(selection == 2):
    print(sb.subtractTwoNums(num1, num2))
elif(selection == 3):
    print(mt.multiplyTwoNums(num1, num2))
elif(selection == 4):
    print(dv.divideTwoNums(num1, num2))
else:
    print('somethings wrong')    