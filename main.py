from classe import Parser

parser = Parser('9_File_judical.txt')
parsed_results = parser.parsed_decisions()

for result in parsed_results:
    print(result)