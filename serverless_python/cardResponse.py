import json
from recyclingCenters import getRecyclingCenters

def getCardContainer(container_type):

	text_containers = {
	    "yellow container": {
	        "text_to_speech": "Yellow containers for cans and cartons",
	        "title": "Yellow containers for cans and cartons",
	        "formatted_text": "Cartons are delivered to sorting plants, which separate the various materials by combining optical, mechanical and manual techniques. The various selected materials are compacted, packaged and distributed to recycling centers.\n    Elements which can be thrown: plastic containers (water bottles, plastic bags, yogurt containers, etc.), beverage and food cans, cartons, plates and metal lids, aluminum foil and cling film, polystyrene trays, etc. Elements which cannot be thrown: toys, watering hoses, tubes, materials such as videotapes and CDs, as well as packaging’s from dangerous products (like solvent or paint)",
	        "image_url": "http://ajuntament.barcelona.cat/ecologiaurbana/sfiles/images/foto_contenidor_groc.jpg",
	    },
	    "grey container": {
	        "text_to_speech": "Grey containers for other waste",
	        "title": "Grey containers for other waste",
	        "formatted_text": "This type of containers includes all the waste which has not been collected. This waste are delivered to eco-parks, where it is separated into paper/cardboard, packaging, glass and other materials by several procedures in order to integrate them into the recycling chain. Waste which cannot be recycled should be delivered to landfills or be incinerated. The ideal is that these treatments are only aimed for waste which cannot be reused or recycled.\n     Elements which can be thrown: cigarette ends, sanitary towels, diapers, sweeping debris, cotton, hair, used pens and pencils, animal feaces.\n    Elements which cannot be thrown: tea bags, paper towels and paper towel stained with oil, leftovers (egg shells, shellfish, etc.), which should be thrown into brown containers. Wood remains, CDs, cartons with toxic materials or clothing should be delivered to Green Dots.",
	        "image_url": "http://ajuntament.barcelona.cat/ecologiaurbana/sfiles/images/foto_contenidor_gris.jpg",
	    },
	    "brown container": {
	        "text_to_speech": "Brown containers for organic waste",
	        "title": "Brown containers for organic waste",
	        "formatted_text": "The substances from plants or animals might degrade biologically like food leftovers and gardening remains. It is a very important type of waste, since it means the third part of the waste we generate at home. This waste is delivered to ecoparks, where it becomes compost and biogas.\n    Elements which can be thrown: leftover meat, fish, bread, fruit, vegetables, seafood and nuts, egg shells, corks, tea bags, coffee grounds, paper towels and napkins stained with oil, gardening waste, etc.\n    Elements which cannot be thrown: sweeping debris, hair, diapers and animal feces, which should be thrown into grey containers. Paper and cardboard, which should be thrown into blue containers.",
	        "image_url": "http://ajuntament.barcelona.cat/ecologiaurbana/sfiles/images/foto_contenidor_marro.jpg",
	    },
	    "blue container": {
	        "text_to_speech": "Blue containers for paper and cardboard",
	        "title": "Blue containers for paper and cardboard",
	        "formatted_text": "Paper and cardboard are delivered to recycling plants, where they become large bales of shredded paper. These bales are soaked to get paper pulp, which is strained to filter its ferrous materials. The resulting paste is dried, ironed and turned into reels, which are distributed to paper mills in order to have a new life.\n    Elements which can be thrown: packaging and cardboard boxes, newspapers, magazines, books without wire-o bound, envelopes, paper bags, sheets, wrapping paper, etc.\n    What cannot be thrown: paper and dirty material, such as paper napkins or paper towels stained with oil, should be thrown in to brown containers. Cartons and foil should be thrown into yellow containers.",
	        "image_url": "http://ajuntament.barcelona.cat/ecologiaurbana/sfiles/images/foto_contenidor_blau.jpg",
	    },
	    "green container": {
	        "text_to_speech": "Green containers for glass",
	        "title": "Green containers for glass",
	        "formatted_text": "Recycling glass is delivered to recycling plants, where cleaning materials are extracted with ferric magnets and crushed in order to convert it into powder (selected, clean and ground glass). This enables to manufacture glass packaging exactly like the original ones for bottles, jars, light bulbs, etc.\n    Elements which can be thrown: glass containers and bottles. Elements which cannot be thrown: broken glasses, flat glass, mirrors, ceramic remains, dishes, light bulbs, fluorescent, etc.",
	        "image_url": "http://ajuntament.barcelona.cat/ecologiaurbana/sfiles/images/foto_contenidor_verd.jpg",
	    },
	    "error": {
	        "text_to_speech": "container_type not valid",
	        "title": "",
	        "formatted_text": "",
	        "image_url": "",
	    }
	}

	card_text = text_containers[container_type];
	if not card_text: 
		card_text = text_containers['error'] 

	return json.dumps({
    	"conversationToken": "",
    	"expectUserResponse": True,
    	"expectedInputs": [
	        {
	            "inputPrompt": {
	                "richInitialPrompt": {
	                    "items": [
	                        {
	                            "simpleResponse": {
	                                "textToSpeech": card_text['text_to_speech']
	                            }
	                        },
	                        {
	                            "basicCard": {
	                                "title": card_text['title'],
	                                "formattedText": card_text['formatted_text'],
	                                "image": {
	                                    "url": card_text['image_url'],
	                                    "accessibilityText": ""
	                                },
	                                "imageDisplayOptions": "WHITE" #CROPPED
	                            }
	                        }
	                    ],
	                    "suggestions": []
	                }
	            }
	        }
	    ]
	})


def getCardRecycling(map_obj):

	address = str(map_obj["formatted_address"])
	latitude = str(map_obj["geometry"]["location"]["lng"])
	longitude = str(map_obj["geometry"]["location"]["lat"])


	recyclingCenters = [{
	    "title": "%s" % address,
	    "description": "",
	    "footer": "",
	    "openUrlAction": {
	      "url": "http://www.google.com/maps/place/%s,%s" % (latitude, longitude)
	    }
	}]

	return json.dumps({
	  "conversationToken": "",
	  "expectUserResponse": True,
	  "expectedInputs": [
	    {
	      "inputPrompt": {
	        "richInitialPrompt": {
	          "items": [
	            {
	              "simpleResponse": {
	                "textToSpeech": "Alright! Here are the closest recycling center."
	              }
	            },
	            {
	              "carouselBrowse": {
	                "items": recyclingCenters
	              }
	            }
	          ]
	        }
	      }
	    }
	  ]
	})

#print(getCardRecycling(getRecyclingCenters()))