import web, datetime

db = web.database(host='127.0.0.1', dbn='mysql', db='blog', user='rickey', pw='5201314')

def get_contents():
    return db.select('bbs', order='id DESC')

def get_content(id):
    try:
        return db.select('bbs', where='id=$id', vars=locals())[0]
    except IndexError:
        return None

def get_page(per_page, offset):
    return db.select('bbs', order='id DESC', offset=offset, limit=per_page)

def get_content_count():
    return db.query("SELECT COUNT(*) AS count FROM bbs")[0]

def get_comment(id):
    return db.select('bbscomment', where='articleId=$id', vars=locals())
