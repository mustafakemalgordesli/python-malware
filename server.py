from flask import Flask,request,send_file
import os

app= Flask(__name__)

@app.route('/show')
def show():
    if request.args.get('type') == '1':
       filename = 'images/'+get_latest_image()
    else:
       filename = 'images/'+get_latest_image()
    return send_file(filename, mimetype='image/gif')


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files['file']
    f.save('images/' +(f.filename))
    return 'file uploaded successfully'

@app.route('/uploadtxt', methods=['POST'])
def uploadtxt():
    f = request.files['file']
    f.save('logs/' +(f.filename))
    return 'file uploaded successfully'

@app.route('/')
def index():
    return 'Hello World'
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)

def get_latest_image(path="images"):
    files = os.listdir(path)
    files.sort(key=lambda x: os.path.getmtime(os.path.join(path, x)))
    files.reverse()
    latest_file = files[0]
    return latest_file