from app_store_scraper import AppStore
from pprint import pprint

import json
import pandas as pd
from tqdm import tqdm

import seaborn as sns
import matplotlib.pyplot as plt

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

# from google_play_scraper import Sort, reviews, app


sns.set(style='whitegrid', palette='muted', font_scale=1.2)

file2 = open("covidtracking1.json", "a")


app_packages = [
    'aarogyasetu'
]

mydict={'in':'aarogyasetu',
 'au':'covidsafe', 'at':'apple-store'
}

app_infos = []

for ap in mydict:
  info = AppStore(country=ap,app_name=mydict[ap])
  info.review(how_many=20)
  app_infos.append(info.reviews)

def print_json(json_object):
  json_str = json.dumps(
    json_object,
    indent=2,
    sort_keys=True,
    default=str,
  )
  file2.writelines(json_str)
  print(highlight(json_str, JsonLexer(), TerminalFormatter()))


print_json(app_infos)
