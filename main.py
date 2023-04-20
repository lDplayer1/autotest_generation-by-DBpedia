from request import table_generator
from classes.country import country, query_cities_of_country
import random


global classtype
classtype = country()
print(type(classtype))

def generate_quiz(table_dict):
    while True:
        if classtype.get_name() == "Country":
            country = random.choice([name.replace(' ','_') for name in table_dict.keys()])
            wrongResults = query_cities_of_country(country)
            keyword = country.replace('_',' ')
        else:
            wrongResults = [value for value in table_dict.values()]
        if not wrongResults:
            continue
        question = f"What is the {classtype.get_opt()} of {keyword}? \n"
        options = [table_dict[keyword]]  # Initialized options list with right answer
        if options[0] in wrongResults:
            wrongResults.remove(options[0])
        wrongOpt = random.sample(wrongResults, min(3, len(wrongResults)))  # Random pick 3 wrong answers
        options.extend(wrongOpt)
        random.shuffle(options)  # Random select options
        
        # Transform options into A/B/C/D 
        choices = ["A", "B", "C", "D"]
        options = dict(zip(choices, options))
        options_str = "\n".join([f"{choice}. {option}" for choice, option in options.items()])
        
        return question + options_str

def main():
    quiz_table = table_generator(classtype)
    for i in range(30): print(generate_quiz(quiz_table))


if __name__ == "__main__" :
    main()