import pathlib
import json
import pickle
# yaml sis used as a configuration file and files are saved as yml
import yaml

file_passage = pathlib.Path("./config.yaml").resolve()
text = {'name': 'Dami', 'age': 29, 'children': ['William', 'Wendy'], 0:  'We are here', 1: 'it is okay not to be fine'}

with file_passage.open(mode="w") as f:
    yaml.dump(text, f, sort_keys=True)

with file_passage.open(mode="r", encoding='utf-8') as file:
    pin = yaml.load(file, Loader=yaml.Loader)

print(pin)
