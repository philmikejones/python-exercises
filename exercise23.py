import requests
import sys

script, input_encoding = sys.argv

languages = "https://learnpythonthehardway.org/python3/languages.txt"
languages = requests.get(languages)
languages.encoding = "utf-8"
