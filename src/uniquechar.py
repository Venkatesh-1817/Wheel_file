def unique(s):
    """
    This function is used to find the first non repeating character in a string.
    """
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    for char in s:
        if char_count[char] == 1:
            return char  
    return ""  
