#encoding=utf-8

from scrapy.webservice import JsonRpcResource
from scrapy.utils.engine import get_engine_status

class EngineStatusResource(JsonRpcResource):
    ws_name='enginestatus'

    def __init__(self,crawler,spider_name=None):
        JsonRpcResource.__init__(self,crawler)
        self._spider_name = spider_name
        self.isLeaf = spider_name is not None

    def render_GET(self,txrequest):
        status = get_engine_status(self.crawler.engine)
        if self._spider_name is None:
            return status
        for sp, st in status['spider'].items():
            if sp.name == self._spider_name:
                return st

    def getChild(self,name,txrequest):
        return EngineStatusResource(name,self.crawler)

class StatsResource(JsonRpcResource):
    ws_name='stats'

    def __init__(self,crawler):
        JsonRpcResource.__init__(self,crawler,crawler.stats)


