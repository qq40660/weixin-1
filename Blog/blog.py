import web
import model
import re

urls = (
    '/', 'Index',
    '/(\d+)', 'Pagination',
    '/view/(\d+)', 'View'
)

t_globals = {
    'datestr': web.datestr,
    're': re
}
render = web.template.render('templates', base='base', globals=t_globals)

class Index:
    def GET(self):
        return web.seeother('/1')

class Pagination:
    def GET(self, page=1):
        page = int(page)
        per_page = 10 
        offset = (page - 1) * per_page

        post_contents = model.get_page(per_page, offset) 
        content_count = model.get_content_count() 

        count_of_pages = content_count.count / per_page + 1

        if page > count_of_pages:
            raise web.seeother('/')
        else:
            return render.index(post_contents, count_of_pages, curr_page=page)

class View:
    def GET(self, id):
        post_content = model.get_content(int(id))
        post_comments = model.get_comment(int(id))
        return render.view(post_content, post_comments)


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
