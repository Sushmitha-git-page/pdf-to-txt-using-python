import PyPDF2
file=open('C:/Users/acer/Downloads/all-html-tags-list-with-example-474.pdf','rb')
read=PyPDF2.PdfReader(file)
print(len(read.pages))
obj=read.pages[1]
print(obj.extract_text())
file.close()
