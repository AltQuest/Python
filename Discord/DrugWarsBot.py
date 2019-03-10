# Work with Python 3.6
# @bitcoinjake09 a discord bot wrote for use with drugwars.
import discord

TOKEN = 'DISCORDBOTTOKENHERE'

client = discord.Client()

#how many per msg
howmany = 25

THE_Member_LIST = []
#open and get our gang member list
with open('members.txt', 'r') as f2:
    THE_Member_LIST = f2.readlines()
#print THE_Member_LIST
#print len(THE_Member_LIST)
memList = ""
for AllMems in THE_Member_LIST:
	memList += (str(' ') + str(AllMems))
#THE_Cartel_LIST = "bitcoinjake09 simi"
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
	if message.author == client.user:
        	return
	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
	if message.content.startswith('!help'):
		msg = '{0.author.mention}'.format(message)
		msg += '\n current commands are: !hello \n !help \n !memlist \n !memcheck <usr,usr,usr>'
		await client.send_message(message.channel, msg)
	if message.content.startswith('!memlist'):
		msg = ''
		msg = 'okay {0.author.mention} here is my current member list:'.format(message) + '\n'
		x=1
		y=1
		for mems in THE_Member_LIST:
			msg += (str(x) + str(') ') + str(mems))

			if (x == (howmany*y)):
				await client.send_message(message.channel, msg)
				msg = ''
				y+=1
			x+=1
		await client.send_message(message.channel, msg)
	if message.content.startswith('!memcheck'):
		defperson = [] #defending persons
		HIT_LIST = []
		HIT_LIST = message.content.split(" ") #contents is a list type
		msg = ''
		HIT_LIST.pop(0)
		rem_list = []
		for element in HIT_LIST:
			if element in memList:
				rem_list.append(element)
			else:
				defperson.append(element)

		for r in rem_list:
			msg += 'DO NOT ATTACK THIS MEMBER: ' + r + '\n'
		for d in defperson:
			msg += 'ATTACK NOW: ' + d + '\n'
		await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
