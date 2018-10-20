import json
from classify import classify
from db import getBin



def translate(event, context):
    body_event = json.loads(event["body"])



    print(body_event)

    par = body_event["queryResult"]["parameters"]
    tMaterial = par["original"]
    

    body = {
        "payload": {
        "google": {
          "expectUserResponse": True,
          "richResponse": {
            "items": [
              {
                "simpleResponse": {
                    "textToSpeech": classify(tree, attributes[:], dataset[id])
                 
                }
              }
            ]
          }
        }
      }
    }

    print(body)

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

def getWaste(body_event)
status = body_event["queryResult"]["parameters"]["status"]

# ricerca del waste

file = 'waste.csv'
f = open(file, 'r')
dataset = [[value.strip() for value in line.strip().split(';')] for line in f]
f.close()

# if waste have status
    # if status != '' 
      # prendo la risposta in base allo stato
  # else
   # chiedere lo stato
# else
   # risposta senza stato

  return response


def getStatus(body_event)



