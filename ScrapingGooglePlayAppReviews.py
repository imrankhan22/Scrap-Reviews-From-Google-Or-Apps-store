import json
import pandas as pd
from tqdm import tqdm

import seaborn as sns
import matplotlib.pyplot as plt

from pygments import highlight
from pygments.lexers import JsonLexer
from pygments.formatters import TerminalFormatter

from google_play_scraper import Sort, reviews, app


sns.set(style='whitegrid', palette='muted', font_scale=1.2)

file2 = open("WHOInfo.txt", "a")


app_packages = [
    'org.who.infoapp'
]



app_infos = []

for ap in tqdm(app_packages):
  #info = app(ap, lang='en', country='us')
  info = reviews(ap, lang='en', count=1000000)
  #del info['comments']
  app_infos.append(info)

def print_json(json_object):
  json_str = json.dumps(
    json_object,
    indent=2,
    sort_keys=True,
    default=str,
  )
  file2.writelines(json_str)
  print(highlight(json_str, JsonLexer(), TerminalFormatter()))


print_json(app_infos[0])
