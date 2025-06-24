#Jackie-Merritt_Lab2/Chp3-6/24/2025

#Inputs and Variabls
t = 0
print("Jane's Stuff Store")
print()
p = int(input("How many items would you like to purchase? "))
print()
for num in range(1, p + 1):
    f = input(f'Enter the price of item {num}: ')
    t = float(f) + t
    av = t / num
    print()
print(f'The total cost of your items is ${t:.2f}')
print(f'The average cost of each item is ${av:.2f}')

