from header import *

# Command to shame Miso for not doing his stuff. 

async def encourage(message, args): 
	# take command and @name
	# on command, print encouraging message to @name
	
	user = getmention(message)
	
	if (user == None):
		msg = "This message should be a string in the header. Also you suck."
	else: 
		msg = "You are such a good boi my dude! :wooper:"
	
	await client.send_message(message.channel, msg)