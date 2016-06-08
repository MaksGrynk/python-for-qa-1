
import json


value = {
    'key1': range(10),
    'key2': {
        'key21': 'value1',
        'key22': 12
    },
    'key3': None,
    'key4': True,
}


print(json.dumps(value))


text = '''
{
    "glossary": {
        "title": "example glossary",
        "GlossDiv": {
            "title": "S",
            "GlossList": {
                "GlossEntry": {
                    "ID": "SGML",
                    "SortAs": "SGML",
                    "GlossTerm": "Standard Generalized Markup Language",
                    "Acronym": "SGML",
                    "Abbrev": "ISO 8879:1986",
                    "GlossDef": {
                        "para": "A meta-markup language, used to create markup languages such as DocBook.",
                        "GlossSeeAlso": ["GML", "XML"]
                    },
                    "GlossSee": "markup"
                }
            }
        }
    }
}
'''

data = json.loads(text)
import ipdb; ipdb.set_trace()
print()




