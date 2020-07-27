# i = 1
# while i <= 5:
#     print("*"*i)
#     i += 1

# i = 20
# while i >= 0:
#     if i % 2 == 0:
#         print(i)
#     i -= 1

nums = []
sum = 0
average = 0

while 1:
    ask = input("Enter an INTEGER. Enter no to exit: ")

    if ask.lower() == "no":
        if len(nums) > 0:
            average = sum / len(nums)
        break

    try:
        nums.append(int(ask))
        sum += int(ask)
    except ValueError:
        print("This isn't an int. Why aren't you using a calculator?")
print()
print("This is a list of all the integers you entered:",nums)
print("The sum of the integers is",sum)
print("The average of all the integers is",average)
print("You could have just used a calculator._.")