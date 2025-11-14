"""Recursion exercises."""
import sys
sys.set_int_max_str_digits(5000)


def loop_reverse(s: str) -> str:
    """
    Reverse a string using a loop.

    loop_reverse("hey") => "yeh"
    loop_reverse("aaa") => "aaa"
    loop_reverse("") => ""
    loop_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    new_s = ""
    for intorstr in s:
        new_s = intorstr + new_s
    return new_s


def recursive_reverse(s: str) -> str:
    """
    Reverse a string using recursion.

    recursive_reverse("hey") => "yeh"
    recursive_reverse("aaa") => "aaa"
    recursive_reverse("") => ""
    recursive_reverse("1") => "1"

    :param s: input string
    :return: reversed input string
    """
    if s == "":
        return ""
    first_char = s[0]
    rest_of_the_s = s[1:]
    return recursive_reverse(rest_of_the_s) + first_char


def loop_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using a loop.

    loop_sum(0) => 0
    loop_sum(3) => 6
    loop_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    new_n = 0
    for i in range(1, n + 1):
        new_n += i
    return new_n


def recursive_sum(n: int) -> int:
    """
    Calculate the sum of all numbers up to n (including n) using recursion.

    recursive_sum(0) => 0
    recursive_sum(3) => 6
    recursive_sum(5) => 15

    :param n: the last number to add to the sum
    :return: sum
    """
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)


def sum_digits_recursive(number: int) -> int:
    """
    Return the sum of the digits in number.

    Given a non-negative int n, return the sum of its digits recursively (no loops).

    sum_digits_recursive(123) => 6
    sum_digits_recursive(1) => 1
    sum_digits_recursive(0) => 0
    sum_digits_recursive(999) => 27

    :param number: non-negative number
    :return: sum of digits in the number
    """
    if number == 0:
        return 0
    else:
        return number % 10 + sum_digits_recursive(number // 10)


def pair_star_recursive(s: str) -> str:
    """
    Add star between identical adjacent chars.

    Given a string, compute recursively a new string
    where identical chars that are adjacent in the original string
    are separated from each other by a "*".

    :param s: input string
    :return: string with stars between identical chars.
    """
    if len(s) <= 1:
        return s
    first_char = s[0]
    rest_of_char = pair_star_recursive(s[1:])
    if first_char == rest_of_char[0]:
        return first_char + "*" + rest_of_char
    else:
        return first_char + rest_of_char
