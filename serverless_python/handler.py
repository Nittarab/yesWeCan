import json
from classify import classify
from db import getBin


def translate(event, context):
    print("event: %s" % event)
    print("context: %s" % context)

    body_event = json.loads(event["body"])
    print(body_event)

    parameters = body_event["queryResult"]["parameters"]
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
        body = getWaste(original, waste)
    else:
        body = generateResponse("I don't understund, retray!")


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print("response: %s" % body)

    return response


def getWaste(original, waste):
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
        response = generateResponse("I don't understund, retray")


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
