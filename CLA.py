import socket, ssl, pprint, cPickle, uuid, sys, os

def sendData(msg, socket):
	#DEFINE THINGS HERE
def recieveData(socket):
	#DEFINE THINGS HERE
def listen():
	#LISTEN FOR CONNECTIONS HERE. WHENEVER PASSING AN ARGUMENT TO A FUNCTION, UNPACK IT WITH cPickle.loads
	
#READ THE CONFIG FILES

usernames_passwords = {} #FILL THIS DICTIONARY WITH THE USERS AS KEYS AND PASSWORDS AS PASS
username_validation = {}
ids_voted = []
electionDone = False

def createValidationNumber(username, password, CLIENT_SOCKET):
	if electionDone != False:
		if username in usernames_passwords.keys():
			if username not in username_validation.keys():
				validationNumber = uuid.uuid4()
				username_validation[username] = validationNumber
				sendData(cPickle.loads((True, validationNumber)), CLIENT_SOCKET)
				sendData(cPickle.loads('Validation', validationNumber), CTF_SOCKET)
				return
	sendData(cPickle.loads((False)))
	return
	
def validationVoted(validationNumber):
	if validationNumber not in ids_voted and electionDone not False:
		ids_voted.append(validationNumber)
	sendData(cPickle.loads(True), CTF_SOCKET)
	return
	
def requestResults(CLIENT_SOCKET):
	if electionDone == True:
		didVote = []
		didNotVote = []
		for x in usernames_passwords.keys():
			if x in username_validation.keys():
				if username_validation[x] in ids_voted:
					didVote.append(x)
			else:
				didNotVote.append(x)
		sendData(cPickle.loads((True, didVote, didNotVote), CLIENT_SOCKET)
		return
	else:
		sendData(cPickle.loads((False, [], [])), CLIENT_SOCKET)
		return
		
def endElectionSignal():
	electionDone = True
	return