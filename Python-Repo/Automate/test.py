def div42by(divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError as err:
        print("Error : {0}".format(err))

print(div42by(2))
print(div42by(3))
print(div42by(12))
print(div42by(43))
print(div42by(0))

print("----------OK Now----------")
print('how many cats do you have?')
num = input()
try:
    if int(num) > 2:
        print("too many bro")
    else:
        print("cool")
except ValueError as ValErr:
    print("Error : {0}".format(ValErr))
    