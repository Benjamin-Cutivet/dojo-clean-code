
def compute_levenshtein_distance(string1, string2):
    lenstring1, lenstring2 = len(string1), len(string2)
    if lenstring1 == 0:
        return lenstring2
    elif lenstring2 == 0:
        return lenstring1
    elif string1[0] == string2[0]:
        return compute_levenshtein_distance(string1[1:], string2[1:])
    else:
        return 1+min(compute_levenshtein_distance(string1, string2[1:]),
                     compute_levenshtein_distance(string1[1:], string2),
                     compute_levenshtein_distance(string1[1:], string2[1:]))


if __name__ == "__main__":
    assert (compute_levenshtein_distance("Python", "Peithen") == 3)
    assert (compute_levenshtein_distance("Azerty12", "Azerty14") == 1)
    assert (compute_levenshtein_distance("Toto", "toto13") == 3)
    assert (compute_levenshtein_distance("JohnDoe2001", "Johndoe2002") == 2)
