def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = set("aeiou")

    input = list(s.lower())
    output = ""
    first = 0
    last = len(s) - 1

    while first < last:
        if input[first] not in vowels:
            first += 1
        elif input[last] not in vowels:
            last += -1
        else:
            input[first], input[last] = input[last], input[first]
            first += 1
            last += -1
            
    return output.join(input)
