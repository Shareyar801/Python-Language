# symbol for comments.
# \ is symbol for multi line string input but however it will provide output in single line.

def basics_variables():
    age: int = 20
    int_var2 = 2 ** 3
    weight = 88.914
    gender = 'Mm'
    name = "Shammmmryar " \
        "farooqui"  
    married: bool = False

    print("PRINTING DATA OF VARIABLES:")
    print(married)
    print(int_var2)

    print("USING IF ELSE STATEMENT ON VARIABLES:")
    if not age < 18 or age == 18:
        print("Your age is " + str(age) + " so you can vote..")

    elif age < 18:
        print("You are under legal age of 18 to vote.")

    if gender == 'M' and gender != 'F':
        print("You are a male")
    else:
        print("You are a female")   


basics_variables()
