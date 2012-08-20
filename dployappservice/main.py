from flask import Flask, jsonify
from flaskcommand import flask_command
from flask.ext.mongokit import MongoKit, Document


app = Flask(__name__)
db = MongoKit()


class Release(Document):
    __collection__ = 'release'

    use_autorefs = True
    use_schemaless = True

    structure = {
        'env': dict,
        'processes': dict,
    }


class App(Document):
    __collection__ = 'app'

    use_autorefs = True
    use_schemaless = True

    structure = {
        'name': unicode,
        'current': unicode,
        'releases': [Release],
    }


def app_factory(config_path=None):
    if config_path:
        app.config.from_pyfile(config_path)
    db.init_app(app)
    db.register([App, Release])
    return app


@app.route('/')
def index():
    return 'index'


@app.route('/<app_name>')
def get_app(app_name):
    return jsonify({'app': 'hello'})


@app.route('/<app_name>/releases')
def list_releases(app_name):
    return jsonify([{'app': 'hello'}])


@app.route('/<app_name>/releases/start-new', methods=['POST'])
def start_new_release(app_name):
    return jsonify({'app': 'hello'})


@app.route('/<app_name>/releases/commit', methods=['POST'])
def commit_release(app_name):
    return jsonify({'status': 'ok'})


@app.route('/<app_name>/releases/<version>')
def get_release(app_name, version):
    return jsonify({
        'services': {
            'mysql': {
                'HELLO_THERE': 'Hello',
            }
        }
    })


@app.route('/create')
def create_app():
    pass


run = flask_command(factory=app_factory)
