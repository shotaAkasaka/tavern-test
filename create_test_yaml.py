import base64
import datetime
import yaml

def createCheckinDate():
    checkindatetime = datetime.datetime.now() + datetime.timedelta(days=10)
    checkindate = checkindatetime.strftime('%Y%m%d')
    return checkindate

def EncodeBase64():
    userid = "user"
    password = "pass"

    # env change

    s = f'{userid}:{password}'
    return base64.b64encode(s.encode('utf-8')).decode("ascii")

# yaml load
with open('common_base.yaml', 'r+') as yml:
    data = yaml.load(yml)
    data["variables"]["service"]["checkin"] = createCheckinDate()
    data["variables"]["service"]["auth"] = EncodeBase64()
    # print(auth)

with open('common.yaml', 'w') as yml:
    yaml.dump(data, yml, default_flow_style=False)
