import json
# Retrieve semaine_type data from static file
_file = open('plannings/static/json/semaine_type.json')
semaineType = json.load(_file)
_file.close()