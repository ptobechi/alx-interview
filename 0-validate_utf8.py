def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for num in data:
        # Get the 8 least significant bits of the integer
        bin_rep = format(num, '08b')[-8:]

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if bin_rep.startswith('0'):
                # 1-byte character (ASCII)
                continue
            elif bin_rep.startswith('110'):
                num_bytes = 1
            elif bin_rep.startswith('1110'):
                num_bytes = 2
            elif bin_rep.startswith('11110'):
                num_bytes = 3
            else:
                return False
        else:
            # Check that the byte starts with '10'
            if not bin_rep.startswith('10'):
                return False
        num_bytes -= 1

    return num_bytes == 0
