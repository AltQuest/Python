#big thanks to https://steemit.com/@idikuci on this one!!!
from beem.steem import Steem
from beem.nodelist import NodeList

nodes = ['https://steemd.minnowsupportproject.org/']

PK = 'posting key here'
accountname =  'bitcoinjake09'
myPlanet = "P-ZU1H748F2TS"
shipName = "corvette1"
shipCount = 2
sleepAmt = (60 * 60 * 6) #set total time for ships to and back to loop right :p
count = 0
# Address of person I don't like
x = 241
y = -41
while(count <= 999):
	s = Steem(node = nodes, keys=[PK])
	id = 'nextcolony'
	json_data = {
  "username": accountname,
  "type": "attack",
  "command": {
    "tr_var1": { shipName: { "pos": 1, "n": shipCount } },
    "tr_var2": x,
    "tr_var3": y,
    "tr_var4": myPlanet
  }
}

	print("will sleep now for: ", sleepAmt, " seconds")
	s.custom_json(id, json_data, required_posting_auths=[accountname])
	print json_data
	count+1
	time.sleep(sleepAmt)
