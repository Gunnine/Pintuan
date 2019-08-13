from core.rest_client import RestClient

"""
https://csg.nhsoft.cn/api-docs/index.html
"""


class RefundItem(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(RefundItem, self).__init__(api_root_url, **kwargs)
        self.headers = {
            'X-Mercury-Token': 'a1bbdd80862d946be30a02b4b835e3e7bd9fb828b8143899',
            'X-Mercury-Appid': 'wx70b804871e8cb77f',
            'X-Mercury-Slug': '23297880'
        }

    def get_refund_item_list(self, **kwargs):
        return self.get('/refund_items', headers=self.headers, **kwargs)

    def get_refund_item_detail(self, number, **kwargs):
        return self.get('/refund_items/{}'.format(number), headers=self.headers, **kwargs)

    def batch_agree_refund(self, **kwargs):
        return self.post('/refund_items/agree_refund', headers=self.headers, **kwargs)

    def batch_reject_refund(self, **kwargs):
        return self.post('/refund_items/reject_refund', headers=self.headers, **kwargs)

    def batch_cancel_overtime(self, **kwargs):
        return self.post('/refund_items/cancel_overtime', headers=self.headers, **kwargs)

