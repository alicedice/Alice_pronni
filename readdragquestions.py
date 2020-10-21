import os
import csv
import json
import pandas as pd


PATH = '/Users/cristina/src/Alice_proni/Excel_files/'
file = 'EPgrade1WBDrag.csv'
input_csv_file_path = os.path.join(PATH, file)
activities = []


#Drag and Drop
with open(input_csv_file_path) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    activity = None

    for csv_row in csv_reader:
        #print(csv_row)
        if csv_row["Instruccion"]:
                activities.append({"title": csv_row["Instruccion"],
                                    "questions": []
                })


        else:
            question = {"text": csv_row["opciones"],
            "answer":{
                "text": csv_row["Respuesta "]
            }}
            activities[-1]["questions"].append(question)

#Write the data in a json files
root = {"kind": "dragndrop",
        "title": file,
        "questions": activities
}

json_file_path = "EPgrade1WBDrag.json"
with open(json_file_path, "w") as json_file:
    json_file.write(json.dumps(root,indent=4))
