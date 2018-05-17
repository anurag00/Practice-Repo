import PyPDF2
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

'''
pdfFile = open(r'G:\Pycode\Automate\rent.pdf','rb')
reader = PyPDF2.PdfFileReader(pdfFile)
print(reader.numPages)
page = reader.getPage(0)
print(page.extractText())
'''
#print(reader.getPage(pageNum).extractText())

# Merging two pdfs
logging.debug("Started")
pdf1File = open(r'G:\Pycode\Automate\rent.pdf','rb')
pdf2File = open(r'G:\Pycode\Automate\view.pdf','rb')
logging.debug("opeend")
reader1 = PyPDF2.PdfFileReader(pdf1File)
logging.debug("reader1")
reader2 = PyPDF2.PdfFileReader(pdf2File)
logging.debug("reader2")

writer = PyPDF2.PdfFileWriter()

for pageNum in range(reader1.numPages):
    page = reader1.getPage(pageNum)
    writer.addPage(page)

for pageNum in range(reader2.numPages):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

'''
page1 = reader1.getPage(0)
page2 = reader2.getPage(0)
page1.mergePage(page2)
writer.addPage(page1)
'''
outputFIle = open(r'G:\Pycode\Automate\Combined.pdf','wb')
writer.write(outputFIle)
outputFIle.close()
pdf1File.close()
pdf2File.close()