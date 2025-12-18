import requests
import json

data = requests.get("https://web.archive.org/web/20240929211114/https://fruityvice.com/api/fruit/all")

results = json.loads(data.text)

pd.DataFrame(results)

df2 = pd.json_normalize(results)

df2

cherry = df2.loc[df2["name"] == 'Cherry']
(cherry.iloc[0]['family']) , (cherry.iloc[0]['genus'])

banana = df2.loc[df2["name"] == 'Banana']
banana.iloc[0]['nutritions.calories']
