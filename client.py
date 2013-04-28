import socket, ssl, pprint, cPickle, uuid, sys, os

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
context.load_verify_locations(cafile='crt/cert.pem')
context.verify_mode = ssl.CERT_REQUIRED

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_ssl = context.wrap_socket(sock)
sock_ssl.connect(('localhost', 4444))
print("Connected to server...")
try:
    pprint.pprint(sock_ssl.getpeercert())
finally:
    sock_ssl.close()

def cls():
	os.system('cls' if os.name == 'nt' else 'clear')
	
def sendData(msg, socket):
	#DEFINE THINGS HERE
def recieveData(socket):
	#DEFINE THINGS HERE
	
def main():
	#should have connected by now
	candidates = cPickle.loads(sock_ssl.recv(MSGLEN)) #something wrong with this
	while 1:
		mode = raw_input("What do you want to do?: ")
		if mode == 'Login':
			user = raw_input("Username: ")
			password = raw_input("Password: ")
			userPassString = cPickle.dumps((user, password))
			sendData(('Login', userPassString), CTF_SOCKET)
			response = cPickle.loads(recieveData(CLA_SOCKET))
			if (response[0] == False):
				pprint.pprint("Something went wrong, sorry.")
				continue
			validationTuple = response[1]
			ID = uuid.uuid4()
			for i, x in ennumerate(candidates):
				pprint.pprint(i + ' ' + x)
			vote = raw_input("Number of the person you're voting for: ")
			voteData = cPickle.dumps((ID, int(float(vote)), validationTuple))
			sendData(voteData, CTA_SOCKET)
			if cPickle.loads(recieveData(CTA_SOCKET)) == True:
				pprint.pprint("Your vote has been recorded; your unique ID is : " + ID)
			else:
				pprint.pprint("Something went wrong with your vote. Sorry about that")
			raw_input("Press any key to clear the screen so the next person can logon")
			cls()
		elif mode == 'End':
			sendData(cPickle.dumps('End'), CTA_SOCKET)
			votes = cPickle.loads(recieveData(CTA_SOCKET))
			for x in votes:
				pprint.pprint("Votes for " + x)
				for person in votes[x]:
					pprint.pprint(person)
			sendData(cPickle.dumps(('End')), CTF_SOCKET)
			whoVoted = cPickle.loads(recieveData(CTF_SOCKET))
			pprint.pprint("These people voted:")
			for x in whoVoted[0]:
				pprint.pprint(x)
			pprint.pprint("These people did not vote:")
			for x in whoVoted[1]:
				pprint.pprint(x)
		elif mode == 'Request':
			sendData(cPickle.dumps('Request'), CTA_SOCKET)
			response = cPickle.loads(recieveData(CTA_SOCKET)
			if (response[0] == False):
				pprint.pprint("Election is not over, cannot request this information")
			else:
				for x in response[1]:
					for v in response[1].keys():
						pprint.pprint(v + ": ")
						for w in response[1][v]:
							pprint.pprint(w)
			
		elif mode == 'Quit':
			sys.exit()
				
	
	