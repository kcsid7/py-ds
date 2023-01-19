def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    val = ""
    to_swap = to_swap.upper()

    for letter in phrase:
        if letter.upper() == to_swap:
            letter = letter.swapcase()
        val  = val + letter
        
    return val

