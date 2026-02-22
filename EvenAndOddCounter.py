countoven = 0
countodd = 0

for i in range(5):
    number = int(input(f"Enter number {i+1}: "))
    if number % 2 == 0:
        countoven += 1
    else:
        countodd += 1
print('=' * 24)
print(f"Total oven numbers: {countoven}.")
print(f"total odd numbers: {countodd}.")
print('=' * 24)
print("\nProgram finished.")