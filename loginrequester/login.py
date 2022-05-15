import requests,os,random,string,json
chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url = ''##REQUEST URL

names = json.loads(open('namelist.json').read())

for name in names:
	name_extra = ''.join(random.choice(string.digits))

	username = name.lower() + name_extra + '@gmail.com'
	password = ''.join(random.choice(chars) for i in range(10))

	requests.post(url, allow_redirects=False, data={
		###FORM DATA PART
		'': username,
		'': password
	})
	print (' username %s and  %s' % (username, password))
