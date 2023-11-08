from lib.context import re

class Parser:
    def __init__(self, file):
        self.file = file
        
    def parsed_decisions(self):
        with open(self.file, 'r', encoding='utf-8') as file_txt:
            lines = file_txt.read()
               
            decision_number = r'(?<= № )[М\d (;/)~-]{18,}'
            decision_data = r'(?<=\d{4}) от [\d]+ [а-я]+ [\d]+ г\.(?= по делу)'
            case_number = r'(?<=№ )[\d/-]+ (?=[А-Я])'
            place_of_decision = r'(?<=\d{4}) \D+ (?=  -)'
            judge = r'[А-Я][а-я]+ [А-Я]\.[А-Я]\.'
            
            result_decision_data = re.findall(decision_data, lines)
            result_decision_number = re.findall(decision_number, lines)
            result_case_number = re.findall(case_number, lines)
            result_place_of_decision = re.findall(place_of_decision, lines)
            result_judge = re.findall(judge, lines)
            
            parsed_results = []

            for decision_number, decision_data, case_number, place_of_decision, judge in zip(result_decision_number, result_decision_data, result_case_number, result_place_of_decision, result_judge):
                parsed_results.append((f"Номер решения: {decision_number}, Дата решения: {decision_data}, Номер дела: {case_number}, Место принятия решения: {place_of_decision}  Судья: {judge}"))
            
            return parsed_results
        
        
parser = Parser('9_File_judical.txt')
parsed_results = parser.parsed_decisions()
for result in parsed_results:
    print(result.rstrip())