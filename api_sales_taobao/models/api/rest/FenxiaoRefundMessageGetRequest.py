'''
Created by auto_sdk on 2016.03.17
'''
from base import RestApi
class FenxiaoRefundMessageGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.page_no = None
		self.page_size = None
		self.sub_order_id = None

	def getapiname(self):
		return 'taobao.fenxiao.refund.message.get'
