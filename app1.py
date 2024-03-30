from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    paramx = request.args.get('paramx',"default")
    return f'The value of paramx is: {paramx}'

if __name__ == '__main__':
    app.run(debug=True)