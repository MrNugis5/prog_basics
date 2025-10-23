def create_list_of_two_elements(a: int, b: int) -> list:
    elements = [a, b]
    return elements



create_list_of_two_elements(81, 72)

def create_list_with_edge_elements(elements: list) -> list:
    if len(elements) ==  1:
        return [elements[0], elements[0]]
    else:
        return [elements[0], elements[-1]]


create_list_with_edge_elements([1, 2, 3])

def get_middle_element_of_list(elements: list) -> any:
    if len(elements) == 1:
        return elements[0]
    for num in elements:
        middle = num // 2
        return elements[middle]
    

get_middle_element_of_list([1, 2, 3])

def get_middle_part_of_list(elements: list) -> list:

    
    elements.pop(0), elements.pop(-1)
    return elements


get_middle_part_of_list([1, 2, 3])

def create_new_list_with_added_number(numbers: list, number: int) -> list:
    new_list = [numbers, number]
    return new_list

create_new_list_with_added_number([1, 2, 3], 4)

def swap_edge_elements(elements: list) -> list:
    elements[0], elements[-1] = elements[-1], elements[0]
    return elements

swap_edge_elements([1, 2])

def add_element_in_position(elements: list, new_element: any, position: int) -> list:
    elements.insert(position, new_element)
    return elements


add_element_in_position([1, 2, 3], 2, 2)

def get_repeated_list(elements: list, repetiton: int) -> list:
    """
    Repeat the elements by certain amount of times.

    get_repeated_list([1, 2], 2) => [1, 2, 1, 2]
    get_repeated_list([1], 5) => [1, 1, 1, 1, 1]
    get_repeated_list([1, 2], 0) => []
    """
    [elements] * repetiton
    return elements

get_repeated_list([1, 2], 2)

def remove_first_element_from_list(elements: list) -> None:
    """
    Remove the first element of the list.

    The list will be modified, nothing is returned.
    There is at least 1 element in the list.

    x = [1, 2, 3]
    remove_first_element_from_list(x)
    x => [2, 3]
    """
    elements.pop(0)
    
remove_first_element_from_list([1])