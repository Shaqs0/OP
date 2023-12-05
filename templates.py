class DecisionTemplates:
    decision_number = r'(?<= № )[М\d (;/)~-]{18,}'
    decision_data = r'(?<=\d{4}) от [\d]+ [а-я]+ [\d]+ г\.(?= по делу)'
    case_number = r'(?<=№ )[\d/-]+ (?=[А-Я])'
    place_of_decision = r'(?<=\d{4}) \D+ (?=  -)'
    judge = r'[А-Я][а-я]+ [А-Я]\.[А-Я]\.'