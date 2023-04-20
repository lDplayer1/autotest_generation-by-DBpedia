from SPARQLWrapper import SPARQLWrapper, JSON
import numpy as np
import pandas as pd
import random
sparql = SPARQLWrapper("http://dbpedia.org/sparql")


def table_generator(classtype):
    """
    para: a specific class that announced personally
    return: a table of keywords and options from endpoint of sparql
    """
    keyword = classtype.get_name()
    filter_dict = classtype.get_filters()
    option = classtype.opt
    query = f"""
    SELECT ?{keyword} ?{option} WHERE {{
    ?{keyword} rdf:type <http://dbpedia.org/ontology/{keyword}>.
    """
    for filter_key, filter_value in filter_dict.items():
        if filter_key.find('undefined') < 0:
            query += f"""
            ?{keyword} <http://dbpedia.org/ontology/{filter_key}> ?{filter_key}.
            """
        query += f""" 
        FILTER {filter_value}
        """
    query += f"""
    OPTIONAL {{?{keyword} <http://dbpedia.org/ontology/{option}> ?{option}.
    }}
    }}
    """
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    quiz_dict = {}
    ## An dict where key is the question theme and value is the right option.
    for result in results["results"]["bindings"]:
        quizText = result[keyword]["value"].split("/")[-1].replace("_", " ")
        if quizText.find("History") >= 0:
            continue
        try:
            rightOpt = result[option]["value"].split("/")[-1].replace("_", " ")
        except KeyError:
            continue
        quiz_dict[quizText] = rightOpt
    return quiz_dict