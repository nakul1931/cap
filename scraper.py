import PyPDF2
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
pdfFileObj = open('meetingminutes.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
pageObj = pdfReader.getPage(0)
#print(pageObj.extractText())
count =0
text =""

while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

String="RFP"
for i in range(0, num_pages):
    PageObj = pdfReader.getPage(i)
    print("this is page " + str(i+1))
    Text = PageObj.extractText()
    # print(Text)
    ResSearch = re.search(String, Text)
    print(ResSearch)

# tokens = word_tokenize(text)
# print(tokens)