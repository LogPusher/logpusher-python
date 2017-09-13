#!/usr/bin/python
#-*-coding:utf-8-*-
import datetime, re, md5, urllib, urllib2

class LogPusher:
	API_URL = 'https://api.logpusher.com/api/agent/savelog';
	def __init__(self, email, password, api_key):

		# check params.
		self.validate_params(email, password, api_key)

		self.email = email
		self.password = md5.new(password).hexdigest()
		self.api_key = api_key

	def validate_params(self, email, password, api_key):
		validate_email = re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email)
		if validate_email == None or email.strip() == "":
			raise Exception("%s is not a valid email address" % email)
		elif password.strip() == "":
			raise Exception("Password cannot be empty.")
		elif api_key.strip() == "":
			raise Exception("API KEY cannot be empty.")

	def get_auth_key(self):
		auth_key = self.create_auth_key()
		return auth_key.encode('base64')

	def create_auth_key(self):
		return self.email + "|" + self.password + "|" + datetime.datetime.now().isoformat()

	def push(self, message, source, category, log_type, log_time, created_at, event_id):
		auth_key = self.get_auth_key()
		post_params = {
			'AuthKey': auth_key,
			'ApiKey': self.api_key,
			'LogMessage': message,
			'Source': source,
			'Category': category,
			'LogType': log_type,
			'LogTime': log_time,
			'CreatedDate': created_at,
			'EventId': event_id
		}

		encoded_params = urllib.urlencode(post_params)
		request = urllib2.Request(self.API_URL, encoded_params)
		response = urllib2.urlopen(request).read()
		return response
