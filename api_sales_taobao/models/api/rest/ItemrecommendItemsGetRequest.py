'''
Created by auto_sdk on 2012.03.22
'''
from base import RestApi
class ItemrecommendItemsGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.count = None
		self.ext = None
		self.item_id = None
		self.recommend_type = None

	def getapiname(self):
		return 'taobao.itemrecommend.items.get'
