def factorial(num:int)-> int:
    """
    calaculates n! using recursion
    Args:
         num(int): user input the int number
         returns:
                 num(int):returns the factorial of the number
    """
    if num ==0 :
        return 1
    return num * factorial(num-1) 




def is_prime(num:int) -> bool:
    """
    check for the number is prime or not
    Args:
         num(int): number for check
             returns:
                    bool: true if that prime or false if that not prime
      """
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True



def common_divisor(num1:int,num2:int)-> list[int]:
    """
    this function help to calc the common division
    """
    limit = min(num1,num2)
    divisors = []

    for divisor in range(1,limit+1):
        if num1 % divisor == 0 and num2 % divisor == 0:
            divisors.append(divisor)
    return divisors

