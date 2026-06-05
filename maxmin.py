# MaxMin Calculator
# Returns the maximum and minimum from a list of integers

def max_min_calculator():
    print("Enter a list of integers:")
    list_of_ints = input()
    list_of_ints = list_of_ints[1:-1]
    list_ints = list_of_ints.split(",")
    final_list = []
    for integer in list_ints:
        final_list.append(int(integer))
    final_list.sort()
    max_int = final_list[-1]
    min_int = final_list[0]
    return print([min_int, max_int])


max_min_calculator()
