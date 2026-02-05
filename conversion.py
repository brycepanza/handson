# utility attempt to convert character to number
def atoi(char):
    unicode = ord(char)
    if unicode not in range(ord('0'), ord('9')+1):
        # pass error for not number
        return None
    # send number as integer
    return unicode - ord('0')


def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.
    
    Returns:
        tuple: (bool, int) - (True, characteristic) if valid, (False, 0) if invalid
    """

    sign = 1
    # check for sign of value
    if num_string[0] == '-':
        sign = -1
        num_string = num_string[1:]
    # sign = -1 if num_string[0] == '-' else 1

    # state variable for valid status of input string
    is_valid = True
    # variable for characteristic number
    num = 0
    
    # iterate for characters in string
    for char in num_string:
        # check for reached decimal point
        if char == '.': break

        # get value from character
        curr_num = atoi(char)

        # check for not found
        if curr_num == None:
            # set proper state
            is_valid = False
            num = 0
            # exit procedure
            break
        print(curr_num)
        num = 10 * num + curr_num

    return (is_valid, sign * num)

    

def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.
    
    Returns:
        tuple: (bool, int, int) - (True, numerator, denominator) if valid, (False, 0, 0) if invalid
    """

    # decimal numerator over power of ten
    numerator = 0
    # decimal denominator power of ten 
    denominator = 1

    # function to send failed status to caller
    def exit_with_fail():
        return (False, 0, 0)

    # check for negative value
    if num_string[0] == '-':
        # local assign absolute value
        num_string = num_string[1:]

    decimal_index = None
    # iterate to pass integer section
    for i in range(len(num_string)):
        # check for end of integer 
        if num_string[i] == '.':
            decimal_index = i
            break
        # otherwise check for invalid input
        if atoi(num_string[i]) == None:
            return exit_with_fail()

    # check for failed exit
    if decimal_index == None:
        return exit_with_fail()

    # iterate to find fraction
    for i in range(decimal_index + 1, len(num_string)):
        digit = atoi(num_string[i])
        # check for invalid input
        if digit == None:
            return exit_with_fail()
        # update state
        numerator = 10 * numerator + digit
        denominator = 10 * denominator

    return (True, numerator, denominator)
