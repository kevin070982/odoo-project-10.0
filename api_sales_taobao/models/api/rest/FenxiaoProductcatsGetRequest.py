'''
Created by auto_sdk on 2016.04.06
'''
from base import RestApi
class FenxiaoProductcatsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None

	def getapiname(self):
		return 'taobao.fenxiao.productcats.get'
