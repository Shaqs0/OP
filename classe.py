import re
from templates import DecisionTemplates

class Parser:
    def __init__(self, file):
        self.file = file
        
    def parsed_decisions(self):
        with open(self.file, 'r', encoding='utf-8') as file_txt:
            lines = file_txt.read()

            result_decision_data = re.findall(DecisionTemplates.decision_data, lines)
            result_decision_number = re.findall(DecisionTemplates.decision_number, lines)
            result_case_number = re.findall(DecisionTemplates.case_number, lines)
            result_place_of_decision = re.findall(DecisionTemplates.place_of_decision, lines)
            result_judge = re.findall(DecisionTemplates.judge, lines)
            
            parsed_results = []

            for decision_number, decision_data, case_number, place_of_decision, judge in zip(result_decision_number, result_decision_data, result_case_number, result_place_of_decision, result_judge):
                parsed_results.append((f"Номер решения: {decision_number}, Дата решения: {decision_data}, Номер дела: {case_number}, Место принятия решения: {place_of_decision}  Судья: {judge}"))
            
            return parsed_results