def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    frequencies1 = {}
    frequencies2 = {}
    for letter in str1:
        frequencies1[letter.lower()] = frequencies1.get(letter, 0) + 1

    for letter in str1:
        frequencies2[letter.lower()] = frequencies2.get(letter, 0) + 1

    if len(frequencies1.keys()) != len(frequencies2.keys()):
        return False

    for key in frequencies1:
        if frequencies1[key] != frequencies2[key]:
            return False

    return True
