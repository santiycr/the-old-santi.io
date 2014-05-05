from flask import Flask
from flask import render_template, request, jsonify
from flask.templating import TemplateNotFound
from google.appengine.api import mail

app = Flask(__name__)


@app.route('/contact', methods=['POST'])
def contact():
    mail.send_mail(sender='santi-io@appspot.gserviceaccount.com',
                   reply_to=request.form['email'],
                   to="santiycr@gmail.com",
                   subject="Contact from santi.io",
                   body=request.form['message'])
    return jsonify(ok=True)


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
