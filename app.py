from flask import Flask, request, jsonify
from PyPDF2 import PdfFileReader
from PIL import Image
import base64
import asyncio

app = Flask(__name__)

def readPdf():
    pdfFileObj = open('converted.pdf', 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    firstPage = pdfReader.getPage(0)
    text = firstPage.extractText()
    print(text)
    return firstPage.extractText()

def decodeBase64(base64String):
    with open('decoded.jpeg', 'wb') as newFile:
        newFile.write(base64.b64decode(base64String, validate=True))
    image = Image.open('decoded.jpeg')
    convertedImage = image.convert('RGB')
    convertedImage.save('converted.pdf')

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello", methods=['POST'])
async def hello_there():
    data = request.get_json()
    decodeBase64(data['image'])
    await asyncio.sleep(2)
    text = readPdf()
    await asyncio.sleep(2)
    return jsonify(text)