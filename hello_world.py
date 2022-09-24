# symbol for comments.

age: int = 20
int_var2 = 2 ** 3
weight = 88.914
gender = 'M'
name = "Shammmmryar " \
       "farooqui"  
# multi line string input but however it will provide output in single line.

married: bool = False
about = ["born in Islamabad", "lives in karachi", "previous residence: hyderabad", 2001, 5.8]
about.append('share')
about2: list = about + ["doing bsit"]
list_mein_list = [['a', '1'], ['b', '2']]

print(married)
print(int_var2)
print(about)
print(about2)
print(list_mein_list)

#Negative List Indices: there are 3 intences in this case.
print(about[-2])
print()


if not age < 18 or age == 18:
    print("Your age is " + str(age) + " so you can vote.")
elif age < 18:
    print("You are under legal age of 18 to vote.")

if gender == 'M' and gender != 'F':
    print("You are a male")
else:
    print("You are a female")
