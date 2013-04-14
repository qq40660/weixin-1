import web
import model

urls = (
    '/', 'Index',
    '/view/(\d+)', 'View'
)

t_globals = {
    'datestr': web.datestr
}
render = web.template.render('templates', base='base', globals=t_globals)

class Index:
    def GET(self):
        posts = model.get_posts()
        return render.index(posts)

class View:
    def GET(self, id):
        post = model.get_post(int(id))
        return render.view(post)


app = web.application(urls, globals())

if __name__ == '__main__':
    app.run()
