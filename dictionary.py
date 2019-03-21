# oxford = {
#       "noun" : "name of animal, place or thing",
#       "pronoun" : "used instead of a noun",
#       "adjective" : "used to describe a noun",
#       "verb" : "action word"
# }
# oxford["adjunt"] = "i don't know"

in_class = {
       "chidi":{
           "surnmame" : "igbo",
            "hobbies"  : ["sleeping", "eating","travelling"],
            "phone" : "08062567877"
            },
       "tolu" :{
             "surnmame" : "igbo",
            "hobbies"  : ["coding", "reading complex stuff","writing code"],
            "phone" : "08062567877"           
           },
       "femi" :{
             "surnmame" : "igbo",
            "hobbies"  :  ["speaking grammar", "teaching complex math"],
            "phone" : "08062567877"           
           },
       
        "omotayo" :{
             "surnmame" : "igbo",
            "hobbies"  : ["drinking sweet","chowing biscuit"],
            "phone" : "08062567877"           
           }
    
}

[in_class["tolu"]["hobbies"]].append("running")

print(in_class["tolu"]["hobbies"])


# print(in_class["tolu"]["hobbies"][2])


#CREATING A DICTIONARY

# synonyms = dict([("happy","pleased"),("angry","vexed"),("run","sare")])
# print(synonyms["run"])


#ANOTHER METHOD OF  CREATING DICTIONARY
# products = dict(
#     rice = "200",
#     garri = "2000",
#     meat = dict(  
#         beef = 200,
#         pork = "100",
#         chicken = "1000"
#     ),
#     poundo = "500"
# )

# products["meat"]["beef"] = 500
# products["meat"]["pork"] = "200"
# print(products["meat"]["pork"])