import urllib.request as url
import json
path = "https://api.cricapi.com/v1/series?apikey=8a9ff01d-521c-490d-b826-b6b9e4266a59&offset=0"
response =url.urlopen(path)
data=json.load(response)["data"]

import pandas as pd
df = pd.DataFrame(data)
print(df)