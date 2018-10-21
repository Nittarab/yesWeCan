import json
from classify import classify
from db import getBin
from cardResponse import getCardContainer


def translate(event, context):
    body_event = json.loads(event["body"])

    parameters = body_event["queryResult"]["parameters"]
    SESSION_ID = body_event["session"]
    original = parameters["original"]
    waste = parameters["waste"]
    print(body_event["queryResult"]["outputContexts"])
    print("waste: %s" % waste)
    status = parameters["status"]
    intent = body_event["queryResult"]["intent"]["displayName"]
    print("intent %s" % intent)

    if intent == 'getWaste':
        body = getWaste(SESSION_ID, original, waste, status)
    elif intent == 'getStatus':
        body = getStatus(SESSION_ID, original, waste, status)
    else:
        body = generateResponse(SESSION_ID, {'waste': ''}, "oooh what?")

    print("response for server  %s" % body)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def getWaste(SESSION_ID, original, waste, status):
    output_params = {"waste": waste}

    file = open('waste.csv', 'r')
    dataset = [line.rstrip('\n').split(',') for line in file]
    file.close()

    wastes = []

    for row in dataset:
        if waste in [value.strip() for value in row[4].split('|')]:
            wastes.append(row)

    print("waste array: %s" % wastes)

    if len(wastes) > 1:
        message = "Do you mean " + ' or '.join('**' + value + '**' for value in wastes[3]) + "?"
        return generateResponse(SESSION_ID, output_params, message)
    elif len(wastes) == 1:

        if status != '':
            if status == 'clean':
                return getCardContainer(wastes[0][1].lower())
            elif status == 'dirty':
                return getCardContainer(wastes[0][1].lower())
            else:
                return generateResponse(SESSION_ID, output_params, "Is the " + waste + " clean or dirty?")
        else:
            return generateResponse(SESSION_ID, output_params, "Is the " + waste + " clean or dirty?")

    else:
        print("nessuno mi gestisce2")
        return generateResponse(SESSION_ID, output_params, "Non trovato niente2")

    return generateResponse(SESSION_ID, output_params, "Non trovato niente3")


def getStatus(SESSION_ID, original, waste, status):
    return generateResponse(SESSION_ID, output_params, "Gestire lo status")


def generateResponse(SESSION_ID, output_params, message):
    return {
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

