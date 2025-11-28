"""Solutions to be tested."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    if time >= 18:
        return True
    if time >= 5 and coffee_needed:
        return True
    if time >= 1:
        return False


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == 5 and c == 5:
        return 10
    if a == b and a == c:
        return 5
    if b != a and c != a:
        return 1
    if b == a or c == a:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    big_size = 5
    max_big_used = min(big_baskets, ordered_amount // big_size)
    remaining = ordered_amount - max_big_used * big_size
    if remaining <= small_baskets:
        return remaining
    else:
        return -1








"""Tests for solution."""
from solution import students_study, lottery, fruit_order


def test__students_study__night_with_coffee__no_studying():
    """During night with coffee students do not study."""
    assert students_study(3, True) is False


def test_solve_test_student_study__evening_coffee_false():
    """W."""
    assert students_study(18, False) is True


def test_solve_test_student_study__night_coffee_false():
    """W."""
    assert students_study(1, False) is False


def test_solve_test_student_study_day_coffee_true():
    """W."""
    assert students_study(8, True) is True


def test_solve_test_student_study__day_coffee_false():
    """W."""
    assert students_study(9, False) is False


def test_solve_test_student_study__evening_coffee_true():
    """W."""
    assert students_study(18, True) is True


def test_solve_test_student_study__evening_edge_case_coffee_true():
    """W."""
    assert students_study(18, True) == students_study(24, True) is True


def test_solve_test_student_study__evening_edge_case_coffee_False():
    """W."""
    assert students_study(18, False) == students_study(24, False) is True


def test_solve_test_student_study__night_edge_case_coffee_true():
    """W."""
    assert students_study(1, True) == students_study(4, True) is False


def test_solve_test_student_study__night_edge_case_coffee_false():
    """W."""
    assert students_study(1, False) == students_study(4, False) is False


def test_solve_test_student_study__day_edge_case_coffee_true():
    """W."""
    assert students_study(5, True) == students_study(17, True) is True


def test_solve_test_student_study__day_edge_case_coffee_false():
    """W."""
    assert students_study(5, False) == students_study(17, False) is False


def test_solve_test_lottery__all_fives():
    """W."""
    assert lottery(5, 5, 5) == 10


def test_solve_test_lottery__all_same_positive():
    """W."""
    assert lottery(4, 4, 4) == 5


def test_solve_test_lottery__all_same_negative():
    """W."""
    assert lottery(-1, -1, -1) == 5


def test_solve_test_lottery__all_same_zero():
    """W."""
    assert lottery(0, 0, 0) == 5


def test_solve_test_lottery__a_b_same_c_diff():
    """W."""
    assert lottery(1, 1, 4) == 0


def test_solve_test_lottery__a_c_same_b_diff():
    """W."""
    assert lottery(1, 5, 1) == 0


def test_solve_test_lottery__b_c_same_a_diff():
    """W."""
    assert lottery(2, 3, 3) == 1


def test_solve_test_lottery__all_diff():
    """W."""
    assert lottery(1, 2, 3) == 1


def test_solve_test_fruit_order__all_zero():
    """W."""
    assert fruit_order(0, 0, 0) == 0


def test_solve_test_fruit_order__only_big_exact_match():
    """W."""
    assert fruit_order(0, 1, 5) == 0


def test_solve_test_fruit_order__only_small_not_enough():
    """W."""
    assert fruit_order(1, 0, 3) == -1


def test_solve_testfruit_order__all_positive_exact_match():
    """W."""
    assert fruit_order(2, 2, 12) == 2


def test_solve_test_fruit_order__match_with_more_than_5_smalls():
    """W."""
    assert fruit_order(12, 2, 22) == 12


def test_solve_test_fruit_order__not_enough_with_more_than_5_smalls():
    """W."""
    assert fruit_order(12, 3, 30) == -1


def test_solve_test_fruit_order__use_some_smalls_some_bigs():
    """W."""
    assert fruit_order(12, 5, 35) == 10


def test_solve_test_fruit_order__zero_amount_zero_small():
    """W."""
    assert fruit_order(0, 5, 5) == 0


def test_solve_test_fruit_order__only_small_more_than_required():
    """W."""
    assert fruit_order(6, 0, 5) == 5


def test_solve_test_fruit_order__enough_bigs_not_enough_smalls():
    """W."""
    assert fruit_order(2, 2, 13) == -1


def test_solve_test_fruit_order__only_big_not_enough_but_multiple_of_5():
    """W."""
    assert fruit_order(0, 10, 52) == -1


def test_solve_test_fruit_order__zero_amount_others_not_zero():
    """W."""
    assert fruit_order(1, 5, 0) == 0


def test_solve_test_fruit_order__only_small_exact_match():
    """W."""
    assert fruit_order(10, 0, 10) == 10


def test_solve_test_fruit_order__only_big_more_than_required_no_match():
    """W."""
    assert fruit_order(0, 4, 17) == -1


def test_solve_test_fruit_order__use_all_smalls_some_bigs():
    """W."""
    assert fruit_order(4, 3, 14) == 4


def test_solve_test_fruit_order__use_some_smalls_some_bigs():
    assert fruit_order(3, 2, 12) == 2


def test_solve_test_fruit_order__only_small_not_enough_more_than_5_smalls():
    assert fruit_order(10, 0, 11) == -1


def test_solve_test_fruit_order__use_some_smalls_some_bigs():
    assert fruit_order(10, 3, 13) == 3


def test_solve_test_fruit_order__zero_amount_zero_big():
    assert fruit_order(3, 0, 0) == 0


def test_solve_test_fruit_order__enough_bigs_not_enough_smalls_large_numbers():
    assert fruit_order(2, 600, 1158) == -1


def test_solve_test_fruit_order__zero_amount_zero_small():
    assert fruit_order(0, 3, 0) == 0


def test_solve_test_fruit_order__use_some_smalls_all_bigs():
    assert fruit_order(6, 5, 30) == 5


def test_solve_test_fruitorder__only_big_not_enough_but_multiple_of_5():
    assert fruit_order(0, 35, 180) == -1
    

def test_solve_test_fruit_order__match_large_numbers():
    assert fruit_order(200, 200, 1200) == 200


def test_solve_test_fruit_order__only_big_more_than_required_match():
    assert fruit_order(0, 13, 25) == 0
