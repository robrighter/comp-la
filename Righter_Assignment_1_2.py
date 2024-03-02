# Robert Righter
# Math 5110
# Assignment 1.2

# Part 1 ----------------------------------------------------------------------------------------

available_toppings = ['pepperoni', 'green pepper', 'pineapple', 'ham', 'tomato', 'extra cheese']
requested_toppings = ['garlic', 'green pepper', 'feta', 'sausage', 'ham']


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


results = process_requested_toppings(requested_toppings)
print_results(results)

# Part 2 ----------------------------------------------------------------------------------------

