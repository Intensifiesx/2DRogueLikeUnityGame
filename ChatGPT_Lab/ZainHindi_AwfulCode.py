def apply_rot13(input_string):
    """
    Applies the ROT13 cipher to the input string.

    Args:
        input_string (str): The input string to be encrypted.

    Returns:
        str: The encrypted string using ROT13 cipher.

    Examples:
        >>> apply_rot13("Hello, World!")
        'Uryyb, Jbeyq!'
        >>> apply_rot13("How are you?")
        'Ubj ner lbh?'
    """
    def rot13_char(c):
        """
        Applies ROT13 cipher to a single character.

        Args:
            c (str): The character to be encrypted.

        Returns:
            str: The encrypted character using ROT13 cipher.
        """
        if c.isupper():
            return chr(((ord(c) - 65 + 13) % 26) + 65)
        elif c.islower():
            return chr(((ord(c) - 97 + 13) % 26) + 97)
        else:
            return c

    return "".join(rot13_char(c) for c in input_string)

# Example usage:
input_string = input("Enter a string: ")
print("ROT13:", apply_rot13(input_string))
