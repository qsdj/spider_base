cookie = 'pgv_pvi=5065803776; ptui_loginuin=1104963431@qq.com; pt2gguin=o1104963431; RK=PlyIgqOAZy; ptcz=9826f4ccaaa76eb83ca67de158f2e6d9ea88a1c48770898673c2bcb4846a61f6; MM_WX_NOTIFY_STATE=1; MM_WX_SOUND_STATE=1; webwxuvid=d428e6f9aaa01b109f8a7efeb1f6ba1b78db53dbdca767dc3948e8cfaed2b2a84b4cc7d7edcab8eeb53075ab474d1787; pgv_info=ssid=s8890274974; pgv_pvid=5688695591; o_cookie=1104963431; mm_lang=zh_CN; wxuin=1278146741; wxsid=H+4U+j/zp4rFw9Qz; webwx_data_ticket=gSe3lJipTi9hoQFRMc1Cpu1a; webwx_auth_ticket=CIsBEO33kMcDGoABN+5C/gAxN571a0XUpYI/aRI6o770cUD5Wgd1Rwq2pJPPMJqsGlywScJQ1Jjos2zCBt0SdEhf0uzA95jGKwcubmto9pDg/IR60fV45aP6vT8bz3lyXtBLbnQzc+/PAe+VTs4GcyE3eLsCRX8Qm+73yErFmfP0/8QOhzVONp5Uutk=; login_frequency=1; last_wxuin=1278146741; wxloadtime=1534264182_expired; wxpluginkey=1534238282'

# c = ','.join(cookie.split('; '))
# c = [i for i in cookie.split('; ')]
d = {i.split('=')[0]: i.split('=')[0] for i in [i for i in cookie.split('; ')]}
print(d)