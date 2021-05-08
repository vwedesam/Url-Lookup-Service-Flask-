from flask import Flask, render_template, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///malware.db'
db = SQLAlchemy(app)

# create malware model


class Malwares(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(225), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Malwares %r>' % self.id


@app.route("/test")
def test():

    malwares = Malwares.query.all()

    return render_template('index.html', malwares=malwares)


@app.route("/urlinfo/1/<hostname>", methods=['GET'])
@app.route("/urlinfo/1/<hostname>/<path>", methods=['GET'])
def url_lookup(hostname, path=None):
    malware = True
    # build query strings
    query = "&".join(f"{k}={v}" for k, v in request.args.items())

    # build path and query
    query_path = path+"?"+query if query else path

    url = hostname+"/"+query_path if path else hostname

    malware = Malwares.query.filter_by(url=hostname).first()

    # reponse Format
    if malware:
        return jsonify({"safe": False, "message": url+" is not safe !!!"})
    else:
        return jsonify({"safe": True, "message": url+" is safe !!!"})


@app.route("/update_malwares", methods=['POST'])
def update_urls():

    request_data = request.get_json()

    if 'malwares' in request_data:
        malwares = request_data['malwares']

        # update malwares
        if str(type(malwares)) == "<class 'list'>" and (len(malwares) > 10 or len(malwares) > 1):
            for url in malwares:
                # add new url
                try:
                    db.session.add(Malwares(url=url))
                    db.session.commit()
                except Exception as ex:
                    return jsonify({'status': 'error', 'message': str(ex)})

            return jsonify({'status': 'success'})

        else:
            return jsonify({'status': 'error', 'message': 'malwares fields must be of type "List" and contains 1 to 10 items!!!'})

    else:
        return jsonify({'status': 'error', 'message': ' malwares fields does not exists'})

    return ""


if __name__ == '__main__':
    app.run()
