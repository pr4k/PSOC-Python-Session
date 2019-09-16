#!/usr/bin/env python3

'''
This simple script fetches a Chuck Norris Joke from an API
'''
# Load Required Libraries
import requests
import json

# Defining URL
url = 'https://official-joke-api.appspot.com/random_joke'

# Fetching JSON from the API
fetch_data = requests.get(url)

# The data is in JSON, let's parse the content from the above data
content = json.loads(fetch_data.content)

# Let's print the joke
print (content['setup'], content['punchline'], sep="\n")