from PyPDF2 import PdfFileReader

def readPdf(fileName):
    pdfFileObj = open(fileName, 'rb')
    pdfReader = PdfFileReader(pdfFileObj)
    firstPage = pdfReader.getPage(0)
    print(firstPage.extractText())
    return pdfReader.numPages

def main():
    print(readPdf('lorem.pdf'))

if __name__ == '__main__':
    main()
    print('Done')