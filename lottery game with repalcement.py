import random

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
draw_count = int(input("Enter how many numbers you want to draw: "))

print("Lottery Draw (With Replacement):")
for i in range(draw_count):
    if len(lottery_numbers) == 0:
        print("No more numbers left to draw!")
        break
    picked = random.choice(lottery_numbers)
    print("Number", i+1, ":", picked)
