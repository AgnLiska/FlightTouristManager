import os
from app import create_app, database
from app.model import Tourist, Flight, reservations
from flask_migrate import Migrate

app = create_app('default')
migrate = Migrate(app, database) 


@app.shell_context_processor
def make_shell_context():
    return dict(database=database, Tourist=Tourist, Flight=Flight, reservations=reservations)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug = True)