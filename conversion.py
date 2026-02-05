def main():
    print(characteristic("23.01"))

def characteristic(num_string):
    """
    Extracts the characteristic (integer part) from a number string.
    
    Returns:
        tuple: (bool, int) - (True, characteristic) if valid, (False, 0) if invalid
    """
    
    # attempt to convert character to number
    def atoi(char):
        unicode = ord(char)
        if unicode not in range(ord('0'), ord('9')+1):
            # pass error for not number
            return None
        # send number as integer
        return unicode - ord('0')

    print(atoi('1'))
    print(atoi('0'))
    print(atoi('9'))
    print(atoi('{'))

def mantissa(num_string):
    """
    Extracts the mantissa (fractional part) from a number string.
    
    Returns:
        tuple: (bool, int, int) - (True, numerator, denominator) if valid, (False, 0, 0) if invalid
    """
    pass

if __name__ == "__main__":
    main()
