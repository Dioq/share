import wda

# for debug
# Enable debug will see http Request and Response
# wda.DEBUG = True

wda.DEBUG = False # default False
wda.HTTP_TIMEOUT = 180.0 # default 180 seconds
wda.DEVICE_WAIT_TIMEOUT = 180.0

c = wda.USBClient("58dad54ccf463a7cf3752365408d766808f40ffd", port=8100) # 指定设备 udid 和WDA 端口号

curStatus = c.status()
print("curStatus=%s" % curStatus)

s = c.session('com.hanlee.top') # 打开app

s(xpath('//Window[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[1]/Other[2]/Button[2]')).click()
# s(name="注册").click()