# MARKJOHN OBIAS
# Week 04 - Looping Statements
# Laboratory # 13 - Guided Coding Exercise: for Loop with break and continue

numbers = list(range(1, 11))

for num in numbers:
    if num == 3:
        continue  # Skip the rest of this iteration
    if num == 7:
        break  # Exit the loop completely
    print(num)
