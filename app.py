from flask import Flask, make_response, jsonify, request
#from Backend.import.script import cur, conn

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

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