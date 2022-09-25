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

    print("PRINTING DATA OF VARIABLES:\n")
    print(married)
    print(int_var2)

    print("USING IF ELSE STATEMENT ON VARIABLES:")
    if not age < 18 or age == 18:
        print("Your age is " + str(age) + " so you can vote.")

    elif age < 18:
        print("You are under legal age of 18 to vote.")

    if gender == 'M' and gender != 'F':
        print("You are a male")
    else:
        print("You are a female")   


def list_working():
    about = ["born in Islamabad", "lives in karachi", "previous residence: hyderabad", 2001, 5.8]
    about.append('share')
    about.insert(3, 'share')

    about.pop
    print("\nLIST 01: ABOUT:- ")
    print(about.count('why'))
    print(len(about))
    print(about)

    print("\nLIST 02: ABOUT2:- ")
    about2: list = about + ["doing bsit"]
    about2.remove(2001)
    print(about2)

    #Negative List Indices: there are 3 intences in this case.
    print(about[-2])  #No 1:a specfic value.
    print(about[-3:]) #No 2:last 3 values
    print(about[:-3]) #No 3:first 4(3+0) values.

    print("\nLIST 03: LIST MEIN LIST:- ")
    list_mein_list = [['a', '1'], ['b', '2']]
    list_mein_list.append(['c', '3'])
    list_mein_list[1][0] = 'B'
    print(list_mein_list)
    list_mein_list = [['a', ['2', 2]], ['b', '2']]
    print(list_mein_list)


list_working()
basics_variables()





