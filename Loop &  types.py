result = [pow(x, 2) for x in range(10) if x % 2 == 0]
#syntax: operation to perform, then loop, then condition if there is any
#like this [EXPRESSION for ITEM in LIST <if CONDITIONAL>]
print('For loop for list working or declaretion: ')
print(result)

alist = [15, 16, 19, 17]
print("\nSimple For loop with list: ")
for sf in alist:
    print(sf)

print("\nSimple For loop with range keyword: ")
for i in range(6):
    print(i)
    i += 2

print("\nSimple While loop with range keyword: ")
h: int=0
while(h < 10):
    print(h)
    h += 2

print("\nNested for loop with nested lists:")
project_groups = [["Nehal", "Shareyar"], ["Hasan", "Hannan"]]
for group in project_groups:
    for student in group:
        print(student)

Randoms = [1, 2, -1, 4, -5, 5, 2, -9]
print("\nContinue keyword with for loop: ")
for i in Randoms:
  if i < 0:
    continue
  print(i)
