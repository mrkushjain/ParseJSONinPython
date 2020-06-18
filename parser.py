import json

input_file = open('userdata.json')
users = json.load(input_file)

for user in users:
	print 'User ID:', user['UserId']
	print 'Group ID:', user['GroupId']