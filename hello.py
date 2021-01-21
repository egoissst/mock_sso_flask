from flask import Flask, request, jsonify
from tinydb import TinyDB, Query
import logging

app = Flask(__name__)
db = TinyDB('database/db.json')
webHookdb = TinyDB('database/webHookdb.json')
LOG_FILE_LOC = "./mock_app.log"
User = Query()

# Logging setup
str_format, datefmt = '%(asctime)s: %(levelname)s: %(message)s', '%m/%d/%Y %I:%M:%S %p'
root_logger = logging.getLogger()
handler = logging.FileHandler(LOG_FILE_LOC, 'w', 'utf-8')
handler.setFormatter = logging.Formatter(str_format, datefmt)
root_logger.addHandler(handler)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/add_user', methods=['POST'])
def add_user():
	req_content = request.get_json()
	if ('uid' in req_content) and db.search(User.uid==req_content['uid']):
		logging.info('user already exists with same uid')
		return 0
	return str(db.insert(req_content))

@app.route('/get_user', methods=['GET'])
def get_user():
	search_uid = request.args.get('uid')
	return jsonify(db.search(User.uid==search_uid))

@app.route('/add_forwebHook', methods=['POST'])
def add_forwebHook():
	req_content = request.get_json()
	return str(webHookdb.insert(req_content))

@app.route('/getall_forwebHook', methods=['GET'])
def getall_forwebHook():
	return jsonify(webHookdb.all())

@app.route('/get_forwebHook', methods=['GET'])
def get_forwebHook():
    search_id = request.args.get('id')
    return jsonify(webHookdb.search(User.A_U_I==search_id))


if __name__ == '__main__':
    app.run()
