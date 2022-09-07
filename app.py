from flask import Flask, request
import base64

app = Flask(__name__)

# def readPdf(fileName):
#     pdfFileObj = open(fileName, 'rb')
#     pdfReader = PdfFileReader(pdfFileObj)
#     firstPage = pdfReader.getPage(0)
#     print(firstPage.extractText())
#     return pdfReader.numPages

def decodeBase64(base64String):
    with open('decoded.jpeg', 'wb') as newFile:
        newFile.write(base64.b64decode(base64String))

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello", methods=['POST'])
def hello_there():
    data = request.get_json()
    decodeBase64(data['image'])

    return "Decoded!"