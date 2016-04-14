from paste.gzipper import middleware as GzipMiddleware
from jinja2 import Template
from jinja2 import Environment
from jinja2 import FileSystemLoader
reference_map = {
    """/about/aboutme.html""": """about/aboutme.html""",
    '''/index.html''': '''index.html''',
    '''/''': '''index.html'''
}


# Загружаем файлы, применяя jinja2
def app(environ, start_response):
    path_info = environ["PATH_INFO"]
    if path_info in reference_map.keys():
        status = '200 OK'
        response_headers = [('Content-type', 'text/html')]
        start_response(status, response_headers)
        full_path = reference_map[path_info]
        # Применяем jinja2
        env = Environment(loader=FileSystemLoader("."))
        template = env.get_template(full_path)
        yield template.render().encode('utf-8')
    else:
        status = '404 Page not found'
        response_headers = [('Content-type', 'text/plain')]
        start_response(status, response_headers)
        return ["Запрашиваемая страница не найдена :(".encode("utf-8")]

if __name__ == '__main__':
    from paste import reloader
    from paste.httpserver import serve

    reloader.install()
    serve(app, host='localhost', port=8000)
