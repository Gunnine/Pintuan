from core.rest_client import RestClient

"""
https://csg.nhsoft.cn/api-docs/index.html
"""


class GrouponTeam(RestClient):
    def __init__(self, api_root_url, **kwargs):
        super(GrouponTeam, self).__init__(api_root_url, **kwargs)
        self.headers = {
            'X-Mercury-Token': 'a1bbdd80862d946be30a02b4b835e3e7bd9fb828b8143899',
            'X-Mercury-Appid': 'wx70b804871e8cb77f',
            'X-Mercury-Slug': '23297880'
        }

    def get_groupon_team_list(self, **kwargs):
        return self.get('/groupon_teams', headers=self.headers, **kwargs)
