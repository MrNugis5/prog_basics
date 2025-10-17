#sum between
#def sum_between(start: int, end: int) -> int:
 #    for numbers in range(start, end + 1):
      #  summa = summa + number
#return summa
        
#sum_between(3,5))

#sum of even sumbers
def sum_of_even_numbers(n: int) -> int:
    summa = 0
    for number in range(n + 1):
        if number % 2 == 0:
            summa = summa + number
    return summa

    
#sum of multiples
def sum_of_multiples(n: int, end: int) -> int:
    """
    Return sum of numbers which are multiples of n between 0 and end (included).

    print(sum_of_multiples(3, 10)) => 3 + 6 + 9 = 18
    print(sum_of_multiples(7, 10)) => 7
    print(sum_of_multiples(11, 10)) => 0
    """
    n = 4
    summa = 0
    for number in range(0, end + 3):
        summa = n * number
    return summa
       
    print(sum_of_multiples(3, 10)) 
    print(sum_of_multiples(7, 10)) 
    print(sum_of_multiples(11, 10))

#cross sum
def cross_sum(numbers: str) -> int:
    """
    Return cross sum of numbers.
    
    print(cross_sum("1234")) => 1 + 2 + 3 + 4 = 10
    print(cross_sum("0")) => 0
    print(cross_sum("4129458")) => 33
    """
    summa = 0
    for symbol in numbers:
        summa += int(symbol)
    return summa



#multiple between

def multiply_between(start: int, end: int) -> int:
    """
    Multiply all numbers between start and end (both included).

    print(multiply_between(1, 3)) => 1 * 2 * 3 = 6
    print(multiply_between(4, 14)) => 14529715200
    print(multiply_between(0, 7)) => 0
    """
    summa = 1
    
    for number in range(start, end + 1):
        summa *= number
    return summa
        
#make hola string
def make_hola_string(count: int) -> str:
    """
    Make hola string.
    
    print(make_hola_string(3)) => "holaholahola"
    print(make_hola_string(0)) => ""
    """
    return "hola" * count
           
#compound intrest
def compound_interest(amount: int, years: int, rate: int) -> float:
    """
    Calculate compound interest.
    
    print(compound_interest(100, 2, 2)) => 104.04
    print(compound_interest(2000, 6, 8)) => 3173.748645888
    """
    return amount * (1 + rate / 100) ** years
    



#remove vowels
def remove_vowels(original_string: str) -> str:
    """
    Return the given string without vowels.
    
    print(remove_vowels("tere-tere")) => tr-tr
    print(remove_vowels("hklmn")) => hklmn
    print(remove_vowels("aauuiii")) => ""
    """
    result = ""
    vowel = "aeiouAEIOU"
    for pl in original_string:
        if pl in vowel:
            result += pl
    return result        
    