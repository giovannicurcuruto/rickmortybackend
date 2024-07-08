from flask import Flask, make_response, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from config import Config
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
##Item necessário para o Flask saber como fará a conexão através do SQL-Alchemy
app.config.from_object(Config)

@app.route('/find', methods=['GET'])
def get_all_characters():
    cur.execute('SELECT * from character')
    result_db = cur.fetchall()

    conn.commit()
    return make_response(
        jsonify(
            message = 'List all Characters',
            data = result_db
        )
    )

app.run()