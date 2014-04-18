from flask import Flask
from flask import render_template
from flask.templating import TemplateNotFound
app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def index(name='index'):
    try:
        return render_template(name + '.html')
    except TemplateNotFound:
        return render_template('page-not-found.html'), 404

if __name__ == '__main__':
    app.debug = True
    app.run()
