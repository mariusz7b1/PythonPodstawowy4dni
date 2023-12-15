import json
import pprint

a = '''{
"info": "bbb",
"ver": 31,
"d": [
{"a": 21, "b": {"x": 1, "y": 2}, "c": [9, 8, 7]},
{"a": 17, "b": {"x": 6, "y": 7}, "c": [6, 5, 4]}
]
}'''

d = json.loads(a)

# wypisanie zbioru danych
pprint.pprint(d)

print(d["d"][1]["b"])

d["d"][1]["b"]["x"] = "XXX"


c = json.dumps(d, ensure_ascii=False)
print(c)
