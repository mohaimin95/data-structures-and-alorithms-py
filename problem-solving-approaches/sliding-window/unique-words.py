def unique_words(str):
    temp = ""
    max = ""
    frequencies = {}
    str = str.replace(" ", "")
    for i in range(len(str)):
        letter = str[i].lower()
        if letter not in frequencies:
            frequencies[letter] = 1
            temp += letter
        else:
            if len(temp) > len(max):
                max = temp
            frequencies = {}
            temp = letter
    return max


print(unique_words("aaaagesaahqwertyhza"))
