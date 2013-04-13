import web, datetime

# 改为对应数据 user, pw
db = web.database(host='127.0.0.1', dbn='mysql', db='blog', user='', pw='')

def get_posts():
    return db.select('bbs', order='id DESC')

def get_post(id):
    try:
        return db.select('bbs', where='id=$id', vars=locals())[0]
    except IndexError:
        return None
