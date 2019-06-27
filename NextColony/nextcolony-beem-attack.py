#big thanks to https://steemit.com/@idikuci on this one!!!
from beem.steem import Steem
from beem.nodelist import NodeList

nodes = ['https://steemd.minnowsupportproject.org/']

PK = 'posting key here'
accountname =  'bitcoinjake09'
myPlanet = "P-ZU1H748F2TS"
shipName = "corvette"
shipCount = 2
# Address of person I don't like
x = 241
y = -41

s = Steem(node = nodes, keys=[PK])
id = 'nextcolony'
json_data = {'username': accountname, "type": "attack", "command": {"tr_var1":{shipName:{"Pos":1, "N":shipCount}},"tr_var2":x,"tr_var3": y, "tr_var4":myPlanet}}

s.custom_json(id, json_data, required_posting_auths=[accountname])
print json_data
