# Напишіть програму, що виводить на екран введене з клавіатури
# дійне число з 5 знаками після коми.

x = input("x = ")
# float - перетворює у дійсне, int - перетворює у ціле
y = float(x)
# print("x =", x)
# print("y =", y)
# print("y = {}".format(y))
print(f"y = |{y:0.5f}|")




