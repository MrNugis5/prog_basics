#create_set_from_numbers

def create_set_from_numbers(a: int, b: int, c: int) -> set:
    numbers = (a, b, c)
    result = set(numbers)
    return numbers

create_set_from_numbers(1, 2, 3)

#add_one
def add_one(set_a: set) -> set:
    return {num + 1 for num in set_a}

#print(add_one({1, 2, 3}))

#remove_six

def remove_six(set_a: set) -> set:
    return set_a.discard(6)


#convert_to_set

def convert_to_set(list_a: list) -> set:
    set_a = set(list_a)
    return set_a

#count_unique_elements

def count_unique_elements(input_list: list) -> int:
    input_set = set(input_list)
    return len(input_set)

#common_characters_in_words

def common_characters_in_words(word1: str, word2: str) -> set:
    a = set(word1)
    b = set(word2)
    return a.intersection(b)
    
#exam_conditions_not_met

def exam_conditions_not_met(names1: list, names2: list) -> set:
    a = set(names1)
    b = set(names2)
    return a.symmetric_difference(b)
    
#uninvated_friends_count

def uninvited_friends_count(friends: list, invited: list) -> int:
    a = set(friends)
    b = set(invited)
    not_invated_count = a.difference(b)
    return len(set(not_invated_count))

#contains_duplicates

def contains_duplicates(input_list: list) -> bool:
    """
    Return whether the list contains duplicate elements.

    No loops required.

    contains_duplicates([1, 2, 3]) => False
    contains_duplicates([1, 2, 1]) => True
    contains_duplicates([1, 1]) => True
    contains_duplicates([1]) => False
    contains_duplicates([]) => False
    """
    a = input_list
    b = input_list
    if a.intersection(b):
        return True
    else:
        False
    
print(contains_duplicates([1, 2, 3]))