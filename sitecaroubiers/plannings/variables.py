import json
# Retrieve semaine_type data from static file
_file = open('plannings/static/json/semaine_type.json')
semaineType = json.load(_file)
_file.close()
# Construct template planning for test
templatePlanning = {'college':{}, 'ecole':{}}
for i in range(5):
    templatePlanning['college']['P'+str(i+1)] = {'datedebut':'2023-09-01', 'datefin':'2023-10-28', 'semaines':[]}
    for j in range(12):
        templatePlanning['college']['P'+str(i+1)]['semaines'].append(semaineType)