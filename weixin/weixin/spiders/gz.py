# -*- coding: utf-8 -*-
import scrapy
from kombu.utils import json


class GzSpider(scrapy.Spider):
    name = 'gz'
    allowed_domains = ['wx.qq.com']
    start_urls = ['https://wx.qq.com/']

    cookie = 'pgv_pvi=5065803776; ptui_loginuin=1104963431@qq.com; pt2gguin=o1104963431; RK=PlyIgqOAZy; ptcz=9826f4ccaaa76eb83ca67de158f2e6d9ea88a1c48770898673c2bcb4846a61f6; MM_WX_NOTIFY_STATE=1; MM_WX_SOUND_STATE=1; webwxuvid=d428e6f9aaa01b109f8a7efeb1f6ba1b78db53dbdca767dc3948e8cfaed2b2a84b4cc7d7edcab8eeb53075ab474d1787; pgv_info=ssid=s8890274974; pgv_pvid=5688695591; o_cookie=1104963431; mm_lang=zh_CN; wxuin=1278146741; wxsid=H+4U+j/zp4rFw9Qz; webwx_data_ticket=gSe3lJipTi9hoQFRMc1Cpu1a; webwx_auth_ticket=CIsBEO33kMcDGoABN+5C/gAxN571a0XUpYI/aRI6o770cUD5Wgd1Rwq2pJPPMJqsGlywScJQ1Jjos2zCBt0SdEhf0uzA95jGKwcubmto9pDg/IR60fV45aP6vT8bz3lyXtBLbnQzc+/PAe+VTs4GcyE3eLsCRX8Qm+73yErFmfP0/8QOhzVONp5Uutk=; login_frequency=1; last_wxuin=1278146741; wxloadtime=1534264182_expired; wxpluginkey=1534238282'

    cookie = {i.split('=')[0]: i.split('=')[0] for i in [i for i in cookie.split('; ')]}

    headers = {
        "Referer": "https://wx.qq.com/",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"}

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0], cookies=self.cookie, headers=self.headers, callback=self.parse)

    def parse(self, response):
        talk_url = 'https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxbatchgetcontact?type=ex&r=1534301314562&lang=zh_CN'

        headers = {
            'Host': 'wx.qq.com',
            'Origin': 'https://wx.qq.com',
            'Pragma': 'no-cache',
            'Referer': 'https://wx.qq.com/?&lang=zh_CN',
            'Content-Type': 'application/json;charset=UTF-8'
        }

        # post请求携带的载荷信息
        request_payload ={
            "BaseRequest": {"Uin": 1278146741, "Sid": "FUZ2fkwN45WylC/M",
                             "Skey": "@crypt_f5efb59e_fbd34923e7cba1564734edf7d7b425ac",
                             "DeviceID": "e096394427054475"},
             "Count": 17,
             "List": [
                {"UserName": "@@46057cb073a65a2289d73be18525174d16c7d5f3fa765fa959a2cf748a65b59", "EncryChatRoomId": ""},
                {"UserName": "@@4b5976f4b8ca09628abaebd3c1fad0d2012dcbf391091da0ebe584d45b8fc61", "EncryChatRoomId": ""},
                {"UserName": "@@5d6765aa45bc46bb48fd24ddd1a397907f1d457d911856804fb27448f618f96d", "EncryChatRoomId": ""},
                {"UserName": "@@ec00635a5e7bfab5b3158b1b1e078b9706d77330035dab87fdbe7b28fba1da3e", "EncryChatRoomId": ""},
                {"UserName": "@@5c8caee55d7b1d3fea9ada352977c4fe72d4c563dc301bd1a4d636b22b5e7005", "EncryChatRoomId": ""},
                {"UserName": "@@3e7b58e4eb9dd2152bd2f22d743b08bcfa8386ecdf628d3c3a3868530b6e19f6", "ChatRoomId": ""},
                {"UserName": "@@d6804880d21f69351324db934fd02869f493aa94bef8f1ac4407fdcb13a20e00", "ChatRoomId": ""},
                {"UserName": "@@0ca19761d88551bb91c4a69b9e2e1ab9442e7101387e554fc70fac13ac6627cc", "ChatRoomId": ""},
                {"UserName": "@@cdc3c0c334dba3fd1d944ed0faaf42ee683e546a8367c103a02a4be22b828752", "ChatRoomId": ""},
                {"UserName": "@@b334d62b9463fcecb95f1652f16b521ff0a7b579e7f9f777fc26fa3e8142203a", "ChatRoomId": ""},
                {"UserName": "@@6c1d69392fc2104bb54d8198568958dcbbbb7bb61a5712ece58cfc8977578c28", "ChatRoomId": ""},
                {"UserName": "@@66198a93adf6ce90e5152ea99d1f611cd3bf226081a3d2cc7164980fe09cc812", "ChatRoomId": ""},
                {"UserName": "@@1baaabb6d3e85880497358716b14a2134b996a1bf607c6e6993039cc3cf5601a", "ChatRoomId": ""},
                {"UserName": "@35e00a7a1f93d0167f9eb4a9ea47d9b4", "EncryChatRoomId": ""},
                {"UserName": "@1c994f6d95f37591e4e17599325e4281ac36d64ca1b59af0e89795ce6611efdc","EncryChatRoomId": ""},
                {"UserName": "@7e1b44722e116872875d577d6de6e671", "EncryChatRoomId": ""},
                {"UserName": "@a2934ec403eec724413d68510c5f5a84", "EncryChatRoomId": ""}]}

        # cookie信息
        cookie = 'pgv_pvi=5065803776; ptui_loginuin=1104963431@qq.com; pt2gguin=o1104963431; RK=PlyIgqOAZy; ptcz=9826f4ccaaa76eb83ca67de158f2e6d9ea88a1c48770898673c2bcb4846a61f6; MM_WX_NOTIFY_STATE=1; MM_WX_SOUND_STATE=1; webwxuvid=d428e6f9aaa01b109f8a7efeb1f6ba1b78db53dbdca767dc3948e8cfaed2b2a84b4cc7d7edcab8eeb53075ab474d1787; pgv_info=ssid=s8890274974; pgv_pvid=5688695591; o_cookie=1104963431; mm_lang=zh_CN; wxuin=1278146741; last_wxuin=1278146741; wxsid=FUZ2fkwN45WylC/M; webwx_data_ticket=gScy2XYh6iA3udZj8Y/dhL/D; webwx_auth_ticket=CIsBEPLz2EQagAGFsR11uEm+t3EuqqBQBDhuEjqjvvRxQPlaB3VHCrakk88wmqwaXLBJwlDUmOizbMIG3RJ0SF/S7MD3mMYrBy5ua2j2kOD8hHrR9Xjlo/q9PxvPeXJe0EtudDNz788B75VEkmdBlYDSDuHuGMjZc7kNuvhPaIesGAdrW07RI4ZZJA==; login_frequency=2; wxloadtime=1534297016_expired; wxpluginkey=1534288322'

        cookie = {i.split('=')[0]: i.split('=')[0] for i in [i for i in cookie.split('; ')]}

        yield scrapy.Request(talk_url,
                             method="POST",
                             cookies=cookie,
                             headers=headers,
                             body=json.dumps(request_payload),
                             callback=self.talk_parse,
                             dont_filter=True)

    def talk_parse(self, response):
        print(response.text)
