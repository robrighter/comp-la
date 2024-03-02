# Robert Righter
# Math 5110
# Assignment 1.2

# Part 1 ----------------------------------------------------------------------------------------

print("Question 1: Create a list 'available_toppings' that includes a list of possible pizza toppings for your restaurant.")
available_toppings = ['pepperoni', 'green pepper', 'pineapple', 'ham', 'tomato', 'extra cheese']
print(available_toppings)
print("\n")

print("Question 2: Create a list 'requested_toppings'. The list can contain items from the list of available toppings as well as items not on that list.")
requested_toppings = ['garlic', 'green pepper', 'feta', 'sausage', 'ham']
print(requested_toppings)
print("\n")

def sort_requested_toppings(toppings):
    available = []
    unavailable = []
    for topping in toppings:
        if topping in available_toppings:
            available.append(topping)
        else:
            unavailable.append(topping)
    return available, unavailable


def topping_list_to_string(topping_list):
    if len(topping_list) == 0:
        return ""
    elif len(topping_list) == 1:
        return topping_list[0]
    elif len(topping_list) == 2:
        return topping_list[0] + " and " + topping_list[1]
    else:
        copy = topping_list.copy()
        copy[-1] = "and " + copy[-1]
        return ", ".join(copy)


def run_preparation_step(available, unavailable):
    ret = []
    if len(available) != 0:
        ret.append("Adding "+ topping_list_to_string(available) + " to your pizza.")
    if len(unavailable) == 1:
        ret.append(unavailable[0].capitalize() + " is not available.")
    elif len(unavailable) > 1:
        ret.append(topping_list_to_string(unavailable).capitalize() + " are not available.")
    return ret


def run_ready_step(available):
    if len(available) == 0:
        return ["Your plain cheese pizza is ready."]
    else:
        return ["Your pizza with " + topping_list_to_string(available) + " is ready."]


def process_requested_toppings(toppings):
    available, unavailable = sort_requested_toppings(toppings)
    ret = run_preparation_step(available, unavailable) + run_ready_step(available)
    return ret


def print_results(results):
    for r in results:
        print(r)



print("Question 3: Write a program that will process the list of requested toppings that provides the specified output.")
print("First we run the program with our original available_toppings and requested_toppings list:")
results = process_requested_toppings(requested_toppings)
print_results(results)
print("\n")

print("Question 3a: Suppose tomatoes and bacon are not.")
available_toppings = ["tomatoes"]
requested_toppings = ["tomatoes","bacon"]
print("Program output:")
results = process_requested_toppings(requested_toppings)
print_results(results)
print("\n")

print("Question 3b: If no toppings are requested or if none of the requested toppings are on the list.")
available_toppings = ["do not order this"]
requested_toppings = ["garlic"]
results = process_requested_toppings(requested_toppings)
print_results(results)
print("Now with no requested toppings:")
results = process_requested_toppings(requested_toppings)
print_results(results)
requested_toppings = []
print("\n")

print("Question 3c: Depending on the number of requested toppings which are available, print statements should have commas and 'and' where appropriate.")
available_toppings = ["mushrooms", "tomatoes", "onions", "green peppers", "black olives"]
print_results(process_requested_toppings(["mushrooms"]))
print_results(process_requested_toppings(["mushrooms", "tomatoes"]))
print_results(process_requested_toppings(["mushrooms", "tomatoes", "onions", "green peppers", "black olives"]))
print("\n")


# Part 2 ----------------------------------------------------------------------------------------

def get_next_number_in_sequence(previous_number):
    if previous_number % 2 == 0:
        # even
        return previous_number/2
    else:
        return (previous_number*3)+1

def make_sequence(starting_number):
    ret = [starting_number]
    previous_number = starting_number
    while True:
        previous_number = get_next_number_in_sequence(previous_number)
        ret.append(previous_number)
        if previous_number == 1:
            break
    return ret

def question_4():
    print("Question 4: What comes next if the first value is 9?")
    print("Answer: The next number after 9 is "+ str(get_next_number_in_sequence(9)))
    print("\n")

def question_5a_and_b():
    # determine which numbers in the range 1 to 100 inclusive take the most iterations to 1
    highest_num_iterations = 1
    starting_numbers = [1]
    for i in range(1,101):
        sequence = make_sequence(i)
        if len(sequence) > highest_num_iterations:
            highest_num_iterations = len(sequence)
            starting_numbers = [i]
        elif len(sequence) == highest_num_iterations:
            starting_numbers.append(i)
    print("Question 5a: For all the numbers from 1-10 inclusive, which number or numbers take the most steps to get to 1?")
    print("The number in the range 1-100 (inclusive) that takes the most steps to get to 1 is: " + str(starting_numbers) + ".")
    print("\n")
    print("Question 5b: How many steps are required for 5a?")
    print("It requires "+ str(highest_num_iterations) + " steps to get to 1.")
    print("\n")

def question_5c_and_d():
    largest_number_in_sequence = 1
    starting_numbers = [1]
    for i in range(1, 101):
        previous_number = i
        while True:
            previous_number = get_next_number_in_sequence(previous_number)
            if previous_number > largest_number_in_sequence:
                largest_number_in_sequence = previous_number
                starting_numbers = [i]
            elif previous_number == largest_number_in_sequence:
                starting_numbers.append(i)
            if previous_number == 1:
                break
    print("Question 5c: Of all the numbers from 1-100, what is the largest number that shows in any sequence?")
    print("The largest number that shows in any sequence is " + str(largest_number_in_sequence) + ".")
    print("\n")
    print("Question 5d: Which starting values give sequences that contain the value from 5c?")
    print("This number shows up in the sequences with these starting values: "+ str(starting_numbers) + ".")
    print("\n")


question_4()
question_5a_and_b()
question_5c_and_d()


#diagnostic function to print all sequences
def print_all_sequences():
   sequences = [{'number': i, 'sequence': make_sequence(i) } for i in range(1,101)]
   for sequence in sequences:
       sequence['length'] = len(sequence['sequence'])
       print(sequence)
