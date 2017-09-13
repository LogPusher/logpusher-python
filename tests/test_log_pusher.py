#!/usr/bin/python
#-*-coding:utf-8-*-

import unittest, datetime
from src.log_pusher_client import LogPusher


class test_LogPusher(unittest.TestCase):
	def test_push(self):
		l = LogPusher('hello@logpusher.com', '123456', 'MY_API_KEY')
		log_date = datetime.datetime.now()		
		self.assertEqual(
			l.push(
				"My awesome log message",
				"myawesomesite.com",
				"E-commerce",
				"Notice",
				log_date.strftime('%H:%S'),
				log_date.isoformat(),
				"1"
			),
			'{"message:":"Your PushLog is saved Success."}'
		)

if __name__ == '__main__':
    unittest.main()
