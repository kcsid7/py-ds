def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    if len(str(num1)) != len (str(num2)):
        return False

    def counter(num):
        """Frequency Counter to return the key val pair for nums"""
        count = {}
        for n in num:
            count[n] = count.get(n, 0) + 1
        return count
    
    return counter(str(num1)) == counter(str(num2))
    