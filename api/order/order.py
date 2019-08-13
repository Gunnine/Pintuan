from core.rest_client import RestClient

"""
https://csg.nhsoft.cn/api-docs/index.html
"""


class Order(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(Order, self).__init__(api_root_url, **kwargs)
        self.headers = {
            'X-Mercury-Token': 'a1bbdd80862d946be30a02b4b835e3e7bd9fb828b8143899',
            'X-Mercury-Appid': 'wx70b804871e8cb77f',
            'X-Mercury-Slug': '23297880'
        }

    def get_order_list(self, **kwargs):
        return self.get('/orders', headers=self.headers, **kwargs)

    def get_order_detail(self, number, **kwargs):
        return self.get('/orders/{}'.format(number), headers=self.headers, **kwargs)

    def update_order_info(self, number, **kwargs):
        return self.put('/orders/{}'.format(number), headers=self.headers, **kwargs)

    def get_statistics(self, **kwargs):
        return self.get('/orders/statistics', headers=self.headers, **kwargs)

    def get_export_url(self, **kwargs):
        return self.get('/orders/export', headers=self.headers, **kwargs)

    def get_order_delivery_manage_list(self, **kwargs):
        return self.get('/orders/delivery_manage', headers=self.headers, **kwargs)

    def order_customize_refund(self, number, **kwargs):
        return self.post('/orders/{}/customize_refund'.format(number), headers=self.headers, **kwargs)

    def get_order_remain_refund_amount(self, number, **kwargs):
        return self.get('/orders/{}/remain_refund_amount'.format(number), headers=self.headers, **kwargs)

    def order_batch_hexiao(self, **kwargs):
        return self.post('/orders/hexiao', headers=self.headers, **kwargs)

    def order_import_hexiao(self, **kwargs):
        return self.post('/orders/import_hexiao', headers=self.headers, **kwargs)
