import web

render = web.template.render('templates/')

urls = (
     '/','index',
     'main.html','main'
     )

class index:
	def GET(self):
		return render.index()
class main:
	def GET(self):
		return render.main()

if __name__ == "__main__":
	app = web.application(urls,globals())
	app.run()
		