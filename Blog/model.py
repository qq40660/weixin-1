import web, datetime

db = web.database(host='127.0.0.1', dbn='mysql', db='blog', user='justin', pw='5201314')

def get_contents():
    return db.select('bbs', order='id DESC')

def get_content(id):
    try:
        return db.select('bbs', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def get_comment(id):
    return db.select('bbscomment', where='articleId=$id', vars=locals())
