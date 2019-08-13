from core.rest_client import RestClient

"""
异常单
https://csg.nhsoft.cn/api-docs/index.html
"""


class FailedPush(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(FailedPush, self).__init__(api_root_url, **kwargs)
        self.headers = {
            'X-Mercury-Token': 'a1bbdd80862d946be30a02b4b835e3e7bd9fb828b8143899',
            'X-Mercury-Appid': 'wx70b804871e8cb77f',
            'X-Mercury-Slug': '23297880'
        }

    def get_failed_push_list(self, **kwargs):
        return self.get('/failed_pushes',headers=self.headers, **kwargs)

    def post_batch_retry_push(self, **kwargs):
        return self.post('/failed_pushes/batch_retry', headers=self.headers, **kwargs)

    def post_batch_ignore_push(self, **kwargs):
        return self.post('/failed_pushes/batch_ignore', headers=self.headers ** kwargs)

    def post_batch_cancel_ignore_push(self, **kwargs):
        return self.post('/failed_pushes/batch_cancel_ignore', headers=self.headers, **kwargs)
