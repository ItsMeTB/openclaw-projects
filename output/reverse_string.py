def reverse_string(input_str):
    """
    Reverse the input string and return the result.

    Parameters:
        input_str (str): The string to be reversed.

    Returns:
        str: The reversed string.
    """
    if not isinstance(input_str, str):
        raise ValueError("Input must be a string.")
    return input_str[::-1]