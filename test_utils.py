import base64
import datetime

def createCheckinDate():
    checkindatetime = datetime.datetime.now() + datetime.timedelta(days=10)
    checkindate = checkindatetime.strftime('%Y%m%d')
    return checkindate

def EncodeBase64(userid, password):
    s = f'{userid}:{password}'
    return base64.b64encode(s.encode('utf-8')).decode("ascii")

# print(createCheckinDate())
# print(EncodeBase64('hoge', 'fuga'))

