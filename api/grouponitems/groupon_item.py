from core.rest_client import RestClient

"""
https://csg.nhsoft.cn/api-docs/index.html
"""


class GrouponItem(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(GrouponItem, self).__init__(api_root_url, **kwargs)
        self.headers = {
            'X-Mercury-Token': 'a1bbdd80862d946be30a02b4b835e3e7bd9fb828b8143899',
            'X-Mercury-Appid': 'wx70b804871e8cb77f',
            'X-Mercury-Slug': '23297880'
        }

    def get_groupon_item_list(self, **kwargs):
        return self.get('/groupon_items', headers=self.headers, **kwargs)

    def create_groupon_item(self, **kwargs):
        return self.post('/groupon_items', headers=self.headers, **kwargs)

    def get_groupon_item_detail(self, id, **kwargs):
        """
        https://csg.nhsoft.cn/api-docs/index.html
        :param id: 活动ID
        """
        return self.get('/groupon_items/{}'.format(id), headers=self.headers, **kwargs)

    def update_groupon_item(self, id, **kwargs):
        return self.put('/groupon_items/{}'.format(id), headers=self.headers, **kwargs)

    def set_groupon_item_active_state(self, id, **kwargs):
        return self.put('/groupon_items/{}/active'.format(id), headers=self.headers, **kwargs)
