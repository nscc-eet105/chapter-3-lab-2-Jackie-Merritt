#Jackie-Merritt_Lab2/Chp3-6/24/2025

#Initial inputs

t = 0
print("Jane's Stuff Store")
print()
p = int(input("How many items would you like to purchase? "))
print()

#Math and loop

for num in range(p):
    f = input(f'Enter the price of item {num + 1}: ')
    t = float(f) + t
av = t / num
print()

#output results
    
print(f'The total cost of your items is ${t:.2f}')
print(f'The average cost of each item is ${av:.2f}')

