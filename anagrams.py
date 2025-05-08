def anagrams(string1, string2):
    """doc"""
    string1 = "".join(i for i in string1.lower() if i.isalnum())
    string2 = "".join(i for i in string2.lower() if i.isalnum())
    return sorted(string1) == sorted(string2)
