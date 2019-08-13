from api.failedpush.failed_push import FailedPush
from api.grouponitems.groupon_item import GrouponItem
from api.grouponteam.groupon_team import GrouponTeam
from api.order.order import Order
from api.refunditem.refunditem import RefundItem

class Mercury():
    def __init__(self, **kwargs):
        self.api_root_url = "https://csg.nhsoft.cn/dashboard/api/v1"
        self.failedpush = FailedPush(self.api_root_url,  **kwargs)
        self.grouponitem = GrouponItem(self.api_root_url, **kwargs)
        self.grouponteam = GrouponTeam(self.api_root_url, **kwargs)
        self.order = Order(self.api_root_url, **kwargs)
        self.refunditem = RefundItem(self.api_root_url, **kwargs)


if __name__ == '__main__':
    r = Mercury()
    x = r.failedpush.get_failed_push_list()
    print(x.status_code)

    x = r.grouponitem.get_groupon_item_list()
    print(x.status_code)

    x = r.grouponitem.get_groupon_item_detail(1)
    print(x)

    x = r.grouponteam.get_groupon_team_list()
    print(x.status_code)

