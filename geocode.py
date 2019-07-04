# -*- coding: utf-8 -*-
# 2018/11/13
# @Author: JeremyZ

import requests
import json
from urllib import parse

class TencentGeo(object):
    def result(self, result):
        result = json.dumps(result, indent=1, ensure_ascii=False)
        return result

    def geocode(self, address):
        """
            地址搜索
        :param address: 地址
        :return:
        """
        parameters = {'address': address, 'key': 'O55BZ-U32W4-EPGUV-XKH2T-2H622-RKBAE'}
        base = 'https://apis.map.qq.com/ws/geocoder/v1'
        response = requests.get(base, params=parameters)
        answer = response.json()
        result = self.result(answer)
        return result

    def search(self, keyword):
        """
            腾讯地图地点搜索
        :param keyword: 地域关键词
        :return:
        """
        parameters = {'address': parse.quote(keyword), 'key': 'O55BZ-U32W4-EPGUV-XKH2T-2H622-RKBAE',
                      'boundary': f"region({parse.quote('阳泉')},{0})", 'keyword': "美食"}
        base = 'https://apis.map.qq.com/ws/place/v1/search'
        response = requests.get(base, params=parameters)
        answer = response.json()
        result = self.result(answer)
        return result

if __name__ == '__main__':
    x = TencentGeo()
    x.geocode("阳泉")
    x.search("第二中学")
