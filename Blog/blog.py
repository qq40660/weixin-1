import web
import model
import re

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View'
)

t_globals = {
    'datestr': web.datestr,
    're': re
}
render = web.template.render('templates', base='base', globals=t_globals)

class Index:
    def GET(self):
        post_contents = model.get_contents()
        return render.index(post_contents)

class View:
    def GET(self, id):
        post_content = model.get_content(int(id))
        post_comments = model.get_comment(int(id))
        return render.view(post_content, post_comments)


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
