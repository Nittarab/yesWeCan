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
        body = getWaste(SESSION_ID, original, waste, status)
    elif intent == 'getStatus':
        body = getWaste(SESSION_ID, original, waste, status)
    else:
        body = generateResponse(SESSION_ID, None, "oooh what?")


    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    print("response: %s" % body)

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

    if len(wastes) > 1:
        message = "Do you mean " + ' or '.join('**' + value + '**' for value in wastes[3]) + "?"
        response = generateResponse(SESSION_ID, output_params, message)
    elif len(wastes) == 1:

        if waste[0] != '':
            if status != '':
                if status == 'clean':
                    response = generateResponse(SESSION_ID, output_params, wastes[0][1])
                elif status == 'dirty':
                    response = generateResponse(SESSION_ID, output_params, wastes[0][2])
                else:
                    response = generateResponse(SESSION_ID, output_params, "Is the " + waste + " clean or dirty?")
            else:
                response = generateResponse(SESSION_ID, output_params, "Is the " + waste + " clean or dirty?")
        else:
            response = generateResponse(SESSION_ID, output_params, wastes[0][0])
    else:
        response = generateResponse(SESSION_ID, output_params, "ERRORE!")

    return response


def getStatus(body_event): pass


def generateResponse(SESSION_ID, output_params, message):
    response = {
         "fulfillmentText": "This is a text response",
            "fulfillmentMessages": [
                {
                "card": {
                    "title": "card title",
                    "subtitle": "card text",
                    "imageUri": "https://assistant.google.com/static/images/molecule/Molecule-Formation-stop.png",
                    "buttons": [
                    {
                        "text": "button text",
                        "postback": "https://assistant.google.com/"
                    }
                    ]
                }
                }
            ],
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
    if output_params != None:
        response["outputContexts"] = [
            {
                "name": "projects/yeswecan-ec289/agent/sessions/" + SESSION_ID + "/contexts/context_name",
                "lifespanCount": 5,
                "parameters": output_params

            }
        ]
    return response
