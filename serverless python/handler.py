import json
from classify import classify
from db import getBin

if id != 9999:
                    "textToSpeech": classify(tree, attributes[:], dataset[id])
                  else:
                    "textToSpeech": "BIENE"

def translate(event, context):
    body_event = json.loads(event["body"])
    dataset = [['Recycling Centre', 'gas', 'FALSE', '', 'TRUE', '', ''], ['Recycling Centre', 'liquid', 'FALSE', '', 'TRUE', '', ''], ['Yellow container', 'solid', 'FALSE', 'metal', 'FALSE', 'FALSE', ''], ['Yellow container', 'solid', 'FALSE', 'metal', 'FALSE', 'FALSE', ''], ['Grey container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'TRUE', 'metal', 'TRUE', 'FALSE', 'TRUE'], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'TRUE', 'plastic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'TRUE', 'metal', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'TRUE', 'metal', 'TRUE', 'FALSE', 'TRUE'], ['Blue container', 'solid', 'FALSE', 'paper', 'FALSE', 'FALSE', 'FALSE'], ['Grey container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', 'plastic', 'FALSE', 'FALSE', 'FALSE'], ['Recycling Centre', 'liquid', 'FALSE', '', 'TRUE', 'FALSE', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'FALSE', 'TRUE'], ['Punt verd', 'solid', 'FALSE', '', 'FALSE', 'FALSE', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', 'plastic', 'FALSE', 'FALSE', 'TRUE'], ['Brown container', 'solid', 'FALSE', '', 'FALSE', 'FALSE', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', '', ''], ['Brown container', 'solid', 'FALSE', 'plastic', 'FALSE', '', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', '', 'TRUE', 'FALSE', 'TRUE'], ['Grey container', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', 'organic', 'FALSE', 'TRUE', ''], ['Recycling Centre', 'solid', 'TRUE', 'plastic', 'FALSE', 'FALSE', 'TRUE'], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', 'TRUE'], ['Recycling Centre', 'solid', 'TRUE', '', 'FALSE', '', 'TRUE'], ['Recycling Centre', 'solid', 'TRUE', '', 'FALSE', 'TRUE', 'TRUE'], ['Recycling Centre', 'liquid', 'FALSE', '', 'TRUE', '', 'TRUE'], ['Blue container', 'solid', 'FALSE', '', 'FALSE', '', 'TRUE'], ['Yellow container', 'solid', 'FALSE', 'plastic', 'FALSE', 'TRUE', ''], ["Recycling Centre (only Vall d' Hebron).", 'solid', 'FALSE', '', 'TRUE', 'TRUE', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', '', 'TRUE'], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'TRUE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'TRUE', '', 'TRUE', 'TRUE', 'TRUE'], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'TRUE', 'TRUE'], ['Green container', 'solid', 'FALSE', 'glass', 'FALSE', 'FALSE', 'TRUE'], ['Green container', 'solid', 'FALSE', 'glass', 'FALSE', '', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', '', 'TRUE', 'FALSE', ''], ['Grey container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'liquid', 'FALSE', 'organic', 'TRUE', '', 'TRUE'], ['Recycling Centre', 'liquid', 'FALSE', '', 'TRUE', '', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'TRUE', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'TRUE', 'TRUE'], ['Yellow container', 'solid', 'FALSE', 'plastic', 'FALSE', 'TRUE', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', 'organic', 'TRUE', '', ''], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', '', 'TRUE'], ['Recycling Centre', 'solid', 'TRUE', '', 'FALSE', 'FALSE', 'TRUE'], ['Recycling Centre', 'solid', 'TRUE', '', 'FALSE', 'TRUE', ''], ['Blue container', 'solid', 'FALSE', '', 'FALSE', '', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'TRUE', 'TRUE'], ['Yellow container', 'solid', 'FALSE', 'metal', 'FALSE', '', ''], ['Yellow container', 'solid', 'FALSE', 'metal', 'FALSE', '', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'TRUE', ''], ['Recycling Centre', 'solid', 'TRUE', '', 'FALSE', 'TRUE', 'TRUE'], ['Brown container', 'liquid', 'FALSE', '', 'FALSE', '', 'TRUE'], ['Grey container', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Blue container', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Blue container', 'solid', 'TRUE', '', 'FALSE', '', 'TRUE'], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'TRUE', 'FALSE', ''], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Blue container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Grey container', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'liquid', 'FALSE', '', 'TRUE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', 'plastic', 'FALSE', 'FALSE', ''], ['Yellow container', 'solid', 'FALSE', 'plastic', 'FALSE', 'FALSE', ''], ['Yellow container', 'solid', 'FALSE', 'plastic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', '', ''], ['Grey container', 'solid', 'FALSE', '', 'FALSE', '', ''], ['Recycling Centre', 'solid', 'FALSE', 'metal', 'FALSE', '', ''], ['Brown container', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', '', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'liquid', 'FALSE', '', 'TRUE', '', ''], ['Recycling Centre', 'gas', 'FALSE', '', 'TRUE', '', ''], ['Recycling Centre', 'solid', 'FALSE', 'metal', 'TRUE', '', ''], ['Brown container', 'solid', 'FALSE', '', 'FALSE', '', ''], ['Yellow container', 'solid', 'FALSE', 'metal', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'TRUE', 'metal', 'FALSE', 'TRUE', ''], ['Yellow container', 'solid', 'FALSE', '', 'FALSE', '', 'TRUE'], ['Recycling Centre', 'solid', '', '', 'TRUE', 'FALSE', ''], ['Recycling Centre', 'solid', '', '', 'TRUE', 'FALSE', 'TRUE'], ['Brown container', 'solid', 'FALSE', 'paper', 'FALSE', 'FALSE', 'TRUE'], ['Recycling Centre', 'liquid', 'FALSE', '', 'FALSE', '', 'TRUE'], ['Grey container', 'solid', 'FALSE', 'plastic', 'FALSE', 'FALSE', 'TRUE'], ['Recycling Centre', 'solid', 'FALSE', '', 'TRUE', '', ''], ['Brown container', 'solid', 'FALSE', 'organic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'TRUE', 'plastic', 'FALSE', 'FALSE', ''], ['Recycling Centre', 'solid', 'FALSE', '', 'FALSE', 'TRUE', ''], ['Recycling Centre', 'solid', 'FALSE', 'organic', 'FALSE', '', ''], ['Blue container', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Blue container', 'solid', 'FALSE', '', 'FALSE', 'FALSE', ''], ['Yellow container', 'solid', 'FALSE', 'plastic', 'FALSE', 'FALSE', '']]


    tree = {('chemical', 'categorical', None, 90): {'FALSE': {('material', 'categorical', None, 69): {'': {('big', 'categorical', None, 32): {'FALSE': {('used', 'categorical', None, 11): {'': ('Grey container', 7), 'TRUE': {('electronic', 'categorical', None, 4): {'FALSE': ('Recycling Centre', 3), 'TRUE': ('Recycling Centre', 1)}}}}, '': {('state', 'categorical', None, 13): {'solid': {('used', 'categorical', None, 11): {'': ('Recycling Centre', 6), 'TRUE': ('Recycling Centre', 5)}}, 'liquid': ('Brown container', 2)}}, 'TRUE': ('Recycling Centre', 8)}}, 'organic': {('big', 'categorical', None, 14): {'FALSE': {('used', 'categorical', None, 12): {'': ('Brown container', 10), 'TRUE': ('Grey container', 2)}}, '': ('Brown container', 1), 'TRUE': ('Recycling Centre', 1)}}, 'plastic': {('big', 'categorical', None, 11): {'FALSE': {('used', 'categorical', None, 8): {'': {('electronic', 'categorical', None, 4): {'FALSE': ('Yellow container', 3), 'TRUE': ('Recycling Centre', 1)}}, 'TRUE': {('electronic', 'categorical', None, 3): {'FALSE': ('Recycling Centre', 2), 'TRUE': ('Recycling Centre', 1)}}, 'FALSE': ('Recycling Centre', 1)}}, '': ('Brown container', 1), 'TRUE': ('Yellow container', 2)}}, 'paper': {('used', 'categorical', None, 2): {'FALSE': ('Blue container', 1), 'TRUE': ('Brown container', 1)}}, 'metal': {('electronic', 'categorical', None, 8): {'FALSE': {('big', 'categorical', None, 6): {'FALSE': ('Yellow container', 3), '': ('Yellow container', 3)}}, 'TRUE': ('Recycling Centre', 2)}}, 'glass': ('Green container', 2)}}, 'TRUE': {('big', 'categorical', None, 21): {'': ('Recycling Centre', 9), 'TRUE': {('electronic', 'categorical', None, 2): {'FALSE': ("Recycling Centre (only Vall d' Hebron).", 1), 'TRUE': ('Recycling Centre', 1)}}, 'FALSE': ('Recycling Centre', 10)}}}}
    attributes = ['state', 'electronic', 'material', 'chemical', 'big', 'used']

    print(body_event)

    par = body_event["queryResult"]["parameters"]
    tMaterial = par["original"]
    
    id = getBin(tMaterial)
    print(id)

    body = {
        "payload": {
        "google": {
          "expectUserResponse": True,
          "richResponse": {
            "items": [
              {
                "simpleResponse": {
                  if id != 9999:
                    "textToSpeech": classify(tree, attributes[:], dataset[id])
                  else:
                    "textToSpeech": "BIENE"
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