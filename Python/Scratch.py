import json
import os


os.system('cls') # on windows

print ("Hello world")


# assigns a JSON string to a variable called jess 
jess = '{"name": "Jessica Wilkins", "hobbies": ["music", "watching TV", "hanging out with friends"]}'

'''
jess = """
groceries:
  - C++ 
  - Python
  - C#
  - VB.NET
  - Scala
"""
'''


# parses the data and assigns it to a variable called jess_dict
jess_dict = json.loads(jess)

# Printed output: {"name": "Jessica Wilkins", "hobbies": ["music", "watching TV", "hanging out with friends"]}
print(jess_dict)
