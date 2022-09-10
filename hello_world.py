# symbol for comments.

age: int = 20
int_var2 = 2 ** 3
weight = 88.914
gender = 'M'
name = "Sharyar " \
       "farooqui"  # multi line string input but however it will provide output in single line.
married: bool = False

print(type(married))

if not age < 18 or age == 18:
    print("the are " + str(age) + " so you can vote.")
elif age < 18:
    print("You are under legal age of 18 to vote.")

if gender == 'M' and gender != 'F':
    print("You are a male")
else:
    print("You are a female")
