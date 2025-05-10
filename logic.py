def calculate_grades(student_text, score_text):
    '''calculates grades and partially checks invalid inputs'''
    try:
        total = int(student_text)
        scores = [int(n) for n in score_text.split()]
    except:
        return False, 'Use only numbers for grades.'

    if len(scores) != total:
        return False, 'Enter exactly ' + student_text + ' scores.'

    highest = max(scores)
    result = []

    for score in scores:
        if score >= highest - 10:
            grade = 'A'
        elif score >= highest - 20:
            grade = 'B'
        elif score >= highest - 30:
            grade = 'C'
        elif score >= highest - 40:
            grade = 'D'
        else:
            grade = 'F'
        result.append('Student score: ' + str(score) + ' Grade: ' + grade)

    return True, result
