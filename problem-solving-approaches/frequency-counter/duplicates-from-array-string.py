#finding duplicates from array.
def getDuplicatesFromArray(arr):
    frequencies = {}
    duplicates = []
    for element in arr:
        frequencies[element] = frequencies.get(element, 0) + 1

    for key in frequencies:
        if frequencies.get(key) > 1:
            duplicates.append(key)

    return duplicates


duplicates = getDuplicatesFromArray([1, 2, 3, 4, 4, 5, 6, 6])
print("Duplicates from array: ", duplicates)

#finds duplicates from string
def getDuplicatesFromString(str):
    frequencies = {}
    duplicates = []

    for letter in str:
        frequencies[letter.lower()] = frequencies.get(letter.lower(), 0) + 1

    for key in frequencies:
        if frequencies.get(key) > 1:
            duplicates.append(key)

    return duplicates


print("Duplicates from string:", getDuplicatesFromString("Hello world"))


