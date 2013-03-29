#encoding=utf-8
import os,sys
path = os.path.dirname(os.path.realpath(__file__))

sys.path.append(path)
import web
import hashlib
import xb.weixin as xb
urls = ("/.*","hello")

app = web.application(urls,globals(),autoreload=False)
application = app.wsgifunc()
class hello:
    def GET(self):
        #token = "shahuwang"
        weixin =  web.input()
        signature = weixin.signature
        timestamp = weixin.timestamp
        nonce = weixin.nonce
        echostr = weixin.echostr
        token = weixin.token
        tmpList = [token,timestamp,nonce]
        tmpList.sort()
        tmpstr = tmpList[0]+tmpList[1]+tmpList[2]
        mySha = hashlib.sha1()
        mySha.update(tmpstr)
        hashstr = mySha.hexdigest()
        if hashstr == signature:
            return token+" is cap"
        else:
            return token
    def POST(self):
        requestMsg = web.webapi.data()
        rootObject = xb.parseString(requestMsg)
        answer = '''
 <xml>
 <ToUserName><![CDATA[%s]]></ToUserName>
 <FromUserName><![CDATA[%s]]></FromUserName>
 <CreateTime>12345678</CreateTime>
 <MsgType><![CDATA[text]]></MsgType>
 <Content><![CDATA[content]]></Content>
 <FuncFlag>0</FuncFlag>
 </xml>
'''%(rootObject.FromUserName,rootObject.ToUserName)

        return answer
if __name__=="__main__":
    app.run()

