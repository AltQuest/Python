#!/usr/lib/python
from flask import Flask, request
from beem.steemconnect import SteemConnect
import getpass


app = Flask(__name__)



c = SteemConnect(client_id="drugwars.app", scope="vote,comment,delete_comment,comment_options,custom_json,claim_reward_balance")
# replace test with our wallet password
wallet_password = getpass.getpass('Wallet-Password:')
c.steem.wallet.unlock(wallet_password)

#https://drugwars.io/callback?
@app.route('/')
def index():
    login_url = c.get_login_url(
        "https://drugwars.io/login",
    )
    return "<a href='%s'>Login with SteemConnect</a>" % login_url


@app.route('/welcome')
def welcome():
    access_token = request.args.get("access_token", None)
    name = request.args.get("username", None)
    if c.get_refresh_token:
        code = request.args.get("code")
        refresh_token = c.get_access_token(code)
        access_token = refresh_token["access_token"]
        name = refresh_token["username"]
    elif name is None:
        c.set_access_token(access_token)
        name = c.me()["name"]

    if name in c.steem.wallet.getPublicNames():
        c.steem.wallet.removeTokenFromPublicName(name)
    c.steem.wallet.addToken(name, access_token)
    return "Welcome <strong>%s</strong>!" % name
