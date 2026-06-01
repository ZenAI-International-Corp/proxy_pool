# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     pikachu.py
   Description :   CharlesPikachu freeproxy代理源
   Author :        JHao
   date：          2026/5/31
-------------------------------------------------
   Change Activity:
                   2026/05/31:
-------------------------------------------------
"""
__author__ = 'JHao'

from fetcher.baseFetcher import BaseFetcher
from handler.logHandler import LogHandler
from util.webRequest import WebRequest

logger = LogHandler("fetcher")


class PikachuFetcher(BaseFetcher):
    """CharlesPikachu freeproxy https://github.com/CharlesPikachu/freeproxy"""

    name = "pikachu"
    url = "https://github.com/CharlesPikachu/freeproxy"

    def fetch(self):
        url = "https://raw.githubusercontent.com/CharlesPikachu/freeproxy/master/proxies.json"
        r = WebRequest().get(url, timeout=10, retry_time=1, verify=False)
        try:
            data = r.json
            if not isinstance(data, dict):
                return
            for item in data.get("data", []):
                if not isinstance(item, dict):
                    continue
                protocol = (item.get("protocol") or "").lower()
                if "socks" in protocol:
                    continue
                ip = item.get("ip")
                port = item.get("port")
                if ip and port:
                    yield "%s:%s" % (ip, port)
        except Exception as e:
            logger.error("ProxyFetch - pikachu: %s" % e)


if __name__ == '__main__':
    for proxy in PikachuFetcher().fetch():
        print(proxy)
