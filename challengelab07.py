#! /usr/bin/env python3


people= [{"name": "Christina Koch", "craft": "ISS"}, {"name": "Alexander Skvortsov", "craft": "ISS"}, {"name": "Luca Parmitano", "craft": "ISS"}, {"name": "Andrew Morgan", "craft": "ISS"}, {"name": "Oleg Skripochka", "craft": "ISS"}, {"name": "Jessica Meir", "craft": "ISS"}]

for i in people:
    #print(i['name']+" is on the"+ i['craft'])
    print(f"{i['name']} is on the {i['craft']}")


