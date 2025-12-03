import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass


#@app.route('/')
#def hello():
#    return 'Hello, World!'

import db
db.init_app(app)

import auth
app.register_blueprint(auth.bp)

import blog
app.register_blueprint(blog.bp)
app.add_url_rule('/', endpoint='index')


if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

