
def is_within_epsilon(a, b, epsilon):
    if abs(a - b) <= epsilon:
        return True
    else:
        return False

def question_1():
    a = float(input("Enter a value of a: "))
    b = float(input("Enter a value of b: "))
    q=1
    while not is_within_epsilon(a, q, .0000000001):
        q = b/a
        a = (a+q)/2
    print(q)



# START
# Get the value of a number n
# Set the value of i to 2
# Set the value of f to 1
# While i is less than or equal to n
#   Set the value of f to f * i
#   Set the value of i to i + 1
# Output f
# STOP
def question_2():
    n = float(input("Enter value of n: "))
    i = 2
    f = 1
    while i <= n:
        f = f * i
        i = i + 1
    print(f)


def question_3a(n):
    n = int(n)
    return n/(n+1)

print("Quesiton 3.a:")
print('The value when n 10 = ' + str(question_3a(10)))
print('The value when n 25 = ' + str(question_3a(25)))
print('The value when n 50 = ' + str(question_3a(50)))
print('The value when n 100 = ' + str(question_3a(100)))
print("\n")

def question_3b_LS(n):
    n = int(n)
    accumulator = 0
    for j in range(1, n+1):
        accumulator = accumulator + (1/(j*(j+1)))
    return accumulator

print("Quesiton 3.b:")
print('The value when n 10 = ' + str(question_3b_LS(10)))
print('The value when n 25 = ' + str(question_3b_LS(25)))
print('The value when n 50 = ' + str(question_3b_LS(50)))
print('The value when n 100 = ' + str(question_3b_LS(100)))
print("\n")

def question_3c_SL(n):
    n = int(n)
    accumulator = 0
    for j in range(n, 0, -1):
        accumulator = accumulator + (1 / (j * (j + 1)))
    return accumulator

print("Quesiton 3.c:")
print('The value when n 10 = ' + str(question_3c_SL(10)))
print('The value when n 25 = ' + str(question_3c_SL(25)))
print('The value when n 50 = ' + str(question_3c_SL(50)))
print('The value when n 100 = ' + str(question_3c_SL(100)))
print("\n")


def question_4():
    a = float(input("Enter the value of a: "))
    d = float(input("Enter the value of d: "))
    r = a
    q = 0
    while r >= d:
        r = r - d
        q = q + 1
    print("The value of q = " + str(q))
    print("The value of r = " + str(r))



def question_5a():
    # count multiplication operations
    acc = 0
    for i in range(1,27):
        acc = acc+i
    print(acc)

def question_5b():
    # calculate the multiplication operations for p(7)
    ret = ""
    for i in range(26, 0, -1):
        ret = ret + " + a_{"+str(27-i)+ "} " + str(7**i)
    return ret


print(question_5b())