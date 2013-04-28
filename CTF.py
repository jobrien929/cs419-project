import socket, ssl, pprint, cPickle, uuid, sys

#READ CONFIG FILE
candidates = {} #DICTIONARY OF ALL CANDIDATES
validationNumbers = {}
electionDone = False

def sendData(msg, socket):
	#DEFINE THINGS HERE
def recieveData(socket):
	#DEFINE THINGS HERE
def listen():
	#LISTEN FOR CONNECTIONS HERE. WHENEVER PASSING AN ARGUMENT TO A FUNCTION, UNPACK IT WITH cPickle.loads
	

def sendCandidates(CLIENT_SOCKET):
	sendData(cPickle.dumps(candidates.keys()), CLIENT_SOCKET)
	return

def addValidationNumber(validationTuple):
	if not electionDone and validationTuple not in validationNumbers.keys()
		validationNumbers[validationTuple] = False
	return
	
def vote(ID, vote, validationTuple, CLIENT_SOCKET):
	if not electionDone:
		if validationTuple in validationNumbers.keys() and vote < len(candidates):
			if (validationNumbers[validationTuple] == False:
				sendData(cPickle.dumps(False), CLIENT_SOCKET)
				return
			validationNumbers[validationTuple] = True
			for i, x in ennumerate(keys(candidates)):
				if i == vote:
					candidates[x] = candiates[x] + ID
					break
			sendData(cPickle.dumps(True), CLIENT_SOCKET)
			sendData(cPickle.dumps(('Voted', validationTuple)), CLA_SOCKET)
			return
	sendData(cPickle.dumps(False), CLIENT_SOCKET)
	return

def endElection():
	electionDone = True
	return

def requestResults(CLIENT_SOCKET):
	if not electionDone:
		sendData(cPickle.dumps((False, [])), CLIENT_SOCKET)
	else:
		sendData(cPickle.dumps((True, candidates)), CLIENT_SOCKET)
	return
