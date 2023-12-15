import json
from os import system
from pprint import pprint as format_json

# czyszczenie ekranu

# otworzenie i doczytanie pliku
file_in = 'd:\\dane\\parameters.json'
file_out = 'd:\\dane\\parameters_mod.json'

with open(file_in) as f:
    dane_json_text = f.read()

# konwersja pliku
dane_json = json.loads(dane_json_text)


# wypisanie pliku na ekranie
print('Cały plik')
format_json(dane_json)
print('\n\n')

# wypisanie klucza parameters
print('klucza parameters')
format_json(dane_json['parameters'])
print('\n\n')

# format_json(dane_json['parameters']['bastionEnabled'])

dane_json['parameters']['bastionEnabled'] = {'value': True}
dane_json['parameters']['subnet1_addressRange']['value'] = "172.16.4.0/23"

# format_json(dane_json['parameters']['bastionEnabled'])
# format_json(dane_json['parameters']['subnet1_addressRange'])

print('Cały plik')
format_json(dane_json)
print('\n\n')


dane_json_text = json.dumps(dane_json, indent=4)
print(dane_json_text)
with open(file_out, 'w') as f:
    f.write(dane_json_text)
