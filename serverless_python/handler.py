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
waste = body_event["queryResult"]["parameters"]["waste"]

# ricerca del waste

file = 'waste.csv'
f = open(file, 'r')
dataset = [[value.strip() for value in line.strip().split(';')] for line in f]
f.close()

synonim_dataset = [item[4].split(',') for item in dataset]




for row in dataset:
  if waste in [value.strip() for value in row[4].split(',')]:
    if status != '':
      if status = 'clean':
        response = row[1]
      else:
        response = row[2]
    else:
      #chiedere lo stato
  else:
    response = row[0]

  return response


def getStatus(body_event)



