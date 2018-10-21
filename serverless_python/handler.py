import json
from classify import classify
from db import getBin


# from wordAssociations import GetAssociations, CheckSynonyms


def translate(event, context):
    print("event: %s" % event)
    print("context: %s" % context)

    body_event = json.loads(event["body"])
    print(body_event)

    parameters = body_event["queryResult"]["parameters"]
    queryText = body_event["queryResult"]["queryText"]
    SESSION_ID = body_event["session"]
    original = parameters["original"]
    waste = parameters["waste"]
    status = parameters["status"]
    intent = body_event["queryResult"]["intent"]["displayName"]

    print("parameters: %s" % parameters)
    print("SESSION_ID: %s" % SESSION_ID)
    print("original: %s" % original)
    print("waste: %s" % waste)
    print("status: %s" % status)
    print("intent: %s" % intent)

    if intent == 'getWaste':
        body = getWaste(original, waste, queryText)
    else:
        body = generateResponse("I don't understund, retray!")

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print("response: %s" % body)

    return response


def getWaste(original, waste, queryText):
    output_params = {"waste": waste}

    file = open('waste.csv', 'r')
    dataset = [line.rstrip('\n').split(',') for line in file]
    file.close()

    wastes = []

    for row in dataset:
        if waste in [value.strip() for value in row[4].split('|')]:
            wastes.append(row)

    if len(wastes) > 1:
        message = "Do you mean " + ' or '.join('**' + value + '**' for value in wastes[3]) + "?"
        response = generateResponse(message)


    elif len(wastes) == 1:
        waste = wastes[0][0] or wastes[0][1]
        response = generateResponse(waste)

    else:
        response = CheckSynonyms(queryText)

    return response


def generateResponse(message):
    response = {
        "payload": {
            "google": {
                "expectUserResponse": True,
                "richResponse": {
                    "items": [
                        {
                            "simpleResponse": {
                                "textToSpeech": message
                            }
                        }
                    ]
                }
            }
        }
    }

    return response


#########


from botocore.vendored import requests
import json
import urllib

# from handler import generateResponse

apikey = '9fe97e86-26fe-4537-acbc-21ede80d58f9'


def GetAssociations(word):
    if word == None:
        return []

    url = 'https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + apikey + '&text=' + urllib.parse.quote(
        word.lower()) + '&lang=en&type=stimulus&limit=50&pos=noun,adjective&indent=no'
    r = requests.get(url)

    if r.status_code != 200:
        return []

    return [item['item'].lower() for item in r.json()['response'][0]['items']]


# GetAssociations('banana')

def IsCategory(word, category):
    app_id = '1f8c349e'
    app_key = '85db88df3e07f2a3e5e9d75caf2e3f24'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' + word.lower()
    r = requests.get(url, headers={'app_id': app_id, 'app_key': app_key})

    # print(r)

    if r.status_code != 200:
        return None

    lexicalCategories = []

    for result in r.json()['results']:
        for lexicalEntry in result['lexicalEntries']:
            lexicalCategories.append(lexicalEntry['lexicalCategory'])

    # print(word, lexicalCategories)

    return category in [lexicalCategory.lower() for lexicalCategory in lexicalCategories]


def IsNoun(word):
    return IsCategory(word, 'noun')


def IsAdjective(word):
    return IsCategory(word, 'adjective')


def IsVerb(word):
    return IsCategory(word, 'verb')


# print(IsNoun('banana'))
# print(IsAdjective('banana'))
# print(IsVerb('throw'))

def GetWords(query):
    if query == None:
        return []

    words = query.split()

    nouns = []
    adjectives = []

    for word in words:
        if not (IsNoun(word) and IsAdjective(word)):
            continue
        if IsNoun(word):
            nouns.append(word)
            continue
        if IsAdjective(word):
            adjectives.append(word)
            continue

    for word in nouns:
        # print(word)
        yield GetAssociations(word)

    for word in adjectives:
        # print(word)
        yield GetAssociations(word)


# GetWords('How should I throw a banana?')

def CheckSynonyms(query):
    file = open('waste.csv', 'r')
    dataset = [line.rstrip('\n').split(',') for line in file]
    file.close()
    # print(dataset)

    matches = []
    for words in GetWords(query):
        matches = []
        for word in words:
            # print(word)
            matches += [record for record in dataset if word in record[4].split('|')]
        if len(matches) > 0:
            break

    if len(matches) == 0:
        return generateResponse("I don't understund, retray")
    elif len(matches) == 1:
        return generateResponse(matches[0][0] or matches[0][1])
    elif len(matches) > 1:
        dist = {}
        for match in matches:
            dist[match[0] or match[1]] = dist.get(match[0] or match[1], 0) + 1
        major = max(dist, key=lambda x: dist[x])
        return generateResponse(major)
