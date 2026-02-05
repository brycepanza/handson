def main():
    print(characteristic("231.01"))
    print(characteristic(".9999"))
    print(characteristic("hello world"))
    print(characteristic("-10000.0"))
    print(characteristic("1022a.50"))

    print("Mantissa")
    print(mantissa("233"))
    print(mantissa("23.233434")
    print(mantissa("12.1a24"))
    print(mantissa("00a.122"))

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
    
    # attempt to convert character to number
    def atoi(char):
        unicode = ord(char)
        if unicode not in range(ord('0'), ord('9')+1):
            # pass error for not number
            return None
        # send number as integer
        return unicode - ord('0')

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
    pass

if __name__ == "__main__":
    main()
