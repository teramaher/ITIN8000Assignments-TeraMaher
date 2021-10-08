#import dif files
import csv
import json

#function to go through the files and add them to json
def make_json(dcFilePath, jsonFilePath, marvelFilePath):
    # create a dictionary
    data = {}
    #open the file
    with open(dcFilePath, encoding='utf-8') as csvf:
    #read through the file
        csvReader = csv.DictReader(csvf)
        #loop through the rows
        for rows in csvReader:
        #take out the alignment, eyes, hair, and sex for dictionary
            characteristic = {
                'ALIGN': rows['ALIGN'],
                'EYE': rows['EYE'],
                'HAIR': rows['HAIR'],
                'SEX': rows['SEX'],
            }
            #put the characteristics and the ownership within the character
            data[rows['name']] = {'Ownership': 'DC', 'Characteristic': characteristic}

    #do the same opening but with marvel
    with open(marvelFilePath, encoding='utf-8') as csvf:
        #translate to dict
        csvReader = csv.DictReader(csvf)
        #go through all the rows
        for rows in csvReader:
        #take the alignment, eyes, hair, and sex to put in characteristic dict
            characteristic = {
                'ALIGN': rows['ALIGN'],
                'EYE': rows['EYE'],
                'HAIR': rows['HAIR'],
                'SEX': rows['SEX'],
            }
            #add the characteristic and ownership to the character
            data[rows['name']] = {'Ownership': 'Marvel', 'Characteristic': characteristic}

    #add the hiarchy of the character name
    publisher = {'Character Name': data}


    #dump dict all to the json file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(publisher, indent=4))


#enter all the files
dcFilePath = r'dc-wikia-data.csv'
marvelFilePath = r'marvel-wikia-data.csv'
jsonFilePath = r'ComicCharacters.json'
# Call the files in the function
make_json(dcFilePath, jsonFilePath, marvelFilePath)