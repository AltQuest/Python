#!/usr/bin/python
#@BitcoinJake09 this will attack the defending person(defperson lol) on nextcolony.
from steem import Steem
from steem.transactionbuilder import TransactionBuilder
from steembase import operations
import time
import json

postingPK = 'put posting key here'
account = "bitcoinjake09"
amt = 1
shipName = "corvette"
shipCount = 2
#shipList = { "corvette": { "pos": 1, "n": 2 } }
defperson= "P-ZYMXM0SAB6O"
x = 241
y = -41
s = Steem(keys=[postingPK])
ops = [
    operations.CustomJson(**{
        "from": account,
        "id": "nextcolony",
	"json":{"username": account,
        "type": "attack", "command": {"tr_var1":{shipName:{"Pos":1, "N":shipCount}},"tr_var2":x,"tr_var3": y, "tr_var4":defperson}},
        "required_auths": [],
        "required_posting_auths": [account],
    }),
]

tb = TransactionBuilder()
tb.appendOps(ops)
tb.appendSigner(account, "posting")
tb.sign()
tb.broadcast()
print ("attacking: ", str(defperson), " with: ", shipCount, " ", str(shipName), " ships")




