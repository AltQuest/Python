#big thanks to https://steemit.com/@idikuci on this one!!!
from beem.steem import Steem
from beem.nodelist import NodeList

nodes = ['https://steemd.minnowsupportproject.org/']

PK = 'posting key here'
accountname =  'bitcoinjake09'
myPlanet = "P-Z6AY2BGWNIO"
shipName = "corvette"
shipCount = 3
sleepAmt = ((3244) * 2) #set as (time it takes ships to get to planet + 4 seconds for steem blockchain) *2 for total mission
# can use a seconds calculator if you know your ships time from spycolony distance calculator:
# https://spycolony.herokuapp.com/calc.html
# seconds calculator: https://www.dollartimes.com/calculators/hours-minutes-calculator.htm
count = 1
# Address of person I don't like x/y
x = -24
y = 249
while(count <= 1001):
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
	progressTime=0
	while(progressTime<=sleepAmt):
		print(progressTime,"/",sleepAmt, " until next attack #", (count+1))
		time.sleep(1)
		progressTime = progressTime + 1
	count = count + 1
