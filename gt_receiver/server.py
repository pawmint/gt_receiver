from __future__ import absolute_import

from flask import Flask, Response, abort, request
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from groundtruth import Groundtruth


app = Flask(__name__)
app.config.from_pyfile('config.py')


engine = create_engine('postgresql+psycopg2://%s:%s@%s/%s' %
                       (app.config['USER'], app.config['PASSWORD'],
                        app.config['HOST'], app.config['DBNAME']))
Session = sessionmaker(bind=engine)
session = Session()


@app.route('/groundtruths', methods=['POST'])
def create_groundtruth():
    try:
        groundtruth = Groundtruth(id=request.form['id'],
                                  activity=request.form['activity'],
                                  user=request.form['user'],
                                  date=request.form['date'])
        session.add(groundtruth)
        session.commit()
        return Response(None, status=201)
    except Exception as e:
        print(e)
        abort(403)


if __name__ == '__main__':
    app.run()
