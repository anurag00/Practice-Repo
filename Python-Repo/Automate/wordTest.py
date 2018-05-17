import logging, docx
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

d = docx.Document("G:\Pycode\Automate\demo.docx")
print(d.paragraphs)
print(d.paragraphs[0].text)
p = d.paragraphs[1]
print(p.runs)
print(p.runs[0].text)
print(p.runs[1].text)
print(p.runs[1].bold)
print(p.runs[2].text)
p.runs[2].underline = True  #different text stylea
p.runs[2].text = " and (underlines) some "
p.style = "Title"
d.save("G:\Pycode\Automate\demo.docx")

d = docx.Document()
d.add_paragraph("Hello this is a paragraph")
d.add_paragraph("Hello this another paragraph")
p = d.paragraphs[0]
p.add_run("this is a new run")
p.runs[1].bold = True
d.save("G:\Pycode\Automate\demo2.docx")
