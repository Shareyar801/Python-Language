from cmath import sqrt

def keyword_working(length = 1, width = 2, depth = 3):
    print('keyword working function entered with values of ' , length, width , depth)

def return_working(x=1, y=2, z=3):
    squareX:int = pow(x, x)
    squareY = pow(y, y)
    squareZ = pow(z, z)
    return squareX, squareY, squareZ

print('\nWorking on multiple types of functions: ')
print('\nFunction 01:')
keyword_working()   #with perdeclared values
keyword_working(width=6, depth=5, length=4) #with parameters in different order
keyword_working(9,8,7) #with custom parameters

print('\nFunction 02:')
X, Y, Z = return_working()
print('Z= %s, Y= %s, X= %s' % (X, Y, Z))