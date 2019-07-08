import requests
import time

sites = ["https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=whatsnew", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=guestbook", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=viewprevious", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=aboutus", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=myaccount", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=loginregister", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=supplierlogin", "https://hebert02-badstore.azurewebsites.net/DoingBusiness/contract.doc", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=supplierproc", "https://hebert02-badstore.azurewebsites.net/BadStore_net_v1_2_Manual.pdf", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=cartview", "https://hebert02-badstore.azurewebsites.net/cgi-bin/badstore.cgi?action=search&searchquery=test", "https://hebert02-badstore.azurewebsites.net/images/store1.jpg", "https://hebert02-badstore.azurewebsites.net/images/1000.jpg", "https://hebert02-badstore.azurewebsites.net/images/1003.jpg", "https://hebert02-badstore.azurewebsites.net/images/1005.jpg", "https://hebert02-badstore.azurewebsites.net/images/1008.jpg", "https://hebert02-badstore.azurewebsites.net/images/1009.jpg", "https://hebert02-badstore.azurewebsites.net/images/1011.jpg", "https://hebert02-badstore.azurewebsites.net/images/1012.jpg", "https://hebert02-badstore.azurewebsites.net/images/1014.jpg"]

clicks = 0
rounds = 0
dataSize = 0

while rounds < 1000:
	for site in sites:
		r = requests.get(site, headers={'Cache-Control': 'no-cache'})
		dataSize += len(r.content)
		clicks += 1
		print "clicks = " + str(clicks) + " , dataSize = " + str(round(dataSize/1000000.0,2)) + "MB"
		time.sleep(.05)
	rounds += 1
	print "round = " + str(rounds)