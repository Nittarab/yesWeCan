from botocore.vendored import requests
import json
import urllib
from handler import generateResponse

apikey = '9fe97e86-26fe-4537-acbc-21ede80d58f9'

def GetAssociations(word):
	if word == None:
		return []

	url = 'https://api.wordassociations.net/associations/v1.0/json/search?apikey=' + apikey + '&text=' + urllib.parse.quote(word.lower()) + '&lang=en&type=stimulus&limit=50&pos=noun,adjective&indent=no'
	r = requests.get(url)

	if r.status_code != 200:
		return []

	return [item['item'].lower() for item in r.json()['response'][0]['items']]

# GetAssociations('banana')

def IsCategory(word, category):	
	app_id = '1f8c349e'
	app_key = '85db88df3e07f2a3e5e9d75caf2e3f24'

	url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/' + word.lower()
	r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

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

	# print(matches)

	if len(matches) == 0:
		return generateResponse("I don't understund, retray")
	elif len(matches) == 1: 
		# un match --> chiedo comunque conferma all'utente per sicurezza
		return generateResponse( matches[0][0] or wastes[0][1])
	elif len(matches) > 1: 
		# match multipli --> chiedo all'utente qual è quello giusto
		return generateResponse("I don't understund, retray")


# CheckSynonyms("How should I throw a banana?")