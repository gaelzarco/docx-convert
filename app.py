from flask import ( Flask, request )
from htmldocx import HtmlToDocx 

app = Flask(__name__)

@app.route('/', methods=[ 'POST' ])
def index():
    if request.method =='POST':
        file = request.files['file']
        file.save(file.filename)

        new_parser = HtmlToDocx()
        new_parser.parse_html_file(f'./{file.filename}', f'./output/{file.filename}')

        return f'POST request successful! You submitted {file}.'

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)