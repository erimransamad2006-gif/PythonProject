from flask import Flask, jsonify
app = Flask(__name__)
# http://127.0.0.1:5000/

@app.route('/', methods=['GET'])
def home():
    return jsonify({'data': 'hello world'})

@app.route('/home/<int:num>', methods=['GET'])
def disp(num):
    return jsonify({'data': num ** 2})
#  http://127.0.0.1:5000/home/10
if __name__ == '__main__':
    app.run(debug=True)