import requests

def trace(*args):
  """Used for debug output"""
  #print (*args)  # Comment out this line to remove debug output
  pass


URL = "https://swapi.dev/api/people/?"

# Get data from the web site and put it into Python collections
trace ("Calling", URL)
response = requests.get(URL) # Get data from the URL
response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

# See what the raw data looks like
trace ("\nText returned:", response.text)

# You can also loop through each item (name/value pairs) in the JSON
trace ("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)

people = data["results"]
for person in people:
  print (person["name"]) 

useranswer = input("Which person do you want to learn more about?")
for useranswer in people:
  print (useranswer["gender"]) 
  print (useranswer["height"]) 
  print (useranswer["mass"]) 
  print (useranswer["hair_color"])
  print (useranswer["eye_color"])     
  print (useranswer["birth_year"])
  break

question =input("Do you want to learn about more characters?")
if input == "yes":
  URL = "https://swapi.dev/api/people/?page=2"
  trace ("Calling", URL)
  response = requests.get(URL) # Get data from the URL
  response.raise_for_status()  # Throw an exception if the request failed
  data = response.json()       # Parse the response into JSON
  trace ("\nText returned:", response.text)
  
  trace ("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)

people = data["results"] 
for person in people:
  print (person["name"]) 
useranswer = input("Which person do you want to learn more about?")
for useranswer in people:
  print (useranswer["gender"]) 
  print (useranswer["height"]) 
  print (useranswer["mass"]) 
  print (useranswer["hair_color"])
  print (useranswer["eye_color"])     
  print (useranswer["birth_year"])
  break

name = input("Which person do you want to learn more about? ").lower()
for person in people:
  if person["name"].lower() == name:
    print ("Gender: {}".format(person["gender"])) 
    print ("Height: {}".format(person["height"])) 
    print ("Weight: {}".format(person["mass"])) 
    print ("Hair Color: {}".format(person["hair_color"]))
    print ("Eye Color: {}".format(person["eye_color"]))  
    print ("Birth Year: {}".format(person["birth_year"]))
    break 

#------------------------------------------------------

URL_1 = "https://swapi.dev/api/people/?page=2"

trace ("Calling", URL_1)
response = requests.get(URL_1) # Get data from the URL
response.raise_for_status()  # Throw an exception if the request failed
data = response.json()       # Parse the response into JSON

# See what the raw data looks like
trace ("\nText returned:", response.text)

# You can also loop through each item (name/value pairs) in the JSON
trace ("\nHere are all the kay/value pairs in the JSON response:")
for key, value in data.items():
  trace (key, ": ", value)

question =input("Do you want to learn about more characters? ").lower()
if input == "yes":
  people = data["results"]
  for person in people:
    print (person["name"]) 
  
  name = input("Which person do you want to learn more about? ").lower()
  for person in people:
    if person["name"].lower() == name:
      print ("Gender: {}".format(person["gender"])) 
      print ("Height: {}".format(person["height"])) 
      print ("Weight: {}".format(person["mass"])) 
      print ("Hair Color: {}".format(person["hair_color"]))
      print ("Eye Color: {}".format(person["eye_color"])) 
      print ("Birth Year: {}".format(person["birth_year"]))
      break 
elif input == "no": 
  pass
