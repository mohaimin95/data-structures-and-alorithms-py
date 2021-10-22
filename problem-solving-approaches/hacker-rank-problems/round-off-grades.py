def gradingStudents(grades):
    roundoffs = []
    for grade in grades:
        if grade < 38:
            roundoffs.append(grade)
        else:
            remainder = grade % 5
            if remainder > 2:
                rounded = grade + (5 - remainder)
                roundoffs.append(rounded)
            else:
                roundoffs.append(grade)
    return roundoffs
