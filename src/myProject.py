import json
import csv

#function to read json file
def read_jsonfile(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

#function to read csv file
def read_csvfile(file_path):
    with open(file_path, 'r') as file:
        return list(csv.DictReader(file))

def main():
    ingredients_file = '../data/ingredients.csv'
    preferences_file = '../data/preferences.json'

    ingredients = read_csvfile(ingredients_file)
    preferences = read_jsonfile(preferences_file)


    print("Ingredients:")
    for row in ingredients:
        print(row)

    print("Preferences:", preferences)
    

if __name__ == "__main__":
    print("in main")
    main()