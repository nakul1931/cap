import PyPDF2
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


import os
path, dirs, files = next(os.walk("/home/nakul/Desktop/PdfScraper/Check"))
print(files)
file_count = len(files)
print(file_count)

for x in range(0,file_count):


    
    pdfFileObj = open(files[x],'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    num_pages = pdfReader.numPages
    # print(num_pages)
    # # pageObjl = pdfReader.getPage(0)
    # # print(pageObjl.extractText())
    # pageObj = pdfReader.getPage(0)
    # print(pageObj.extractText())
    # count =0
    # text =""
    # while count < num_pages:
    #     pageObj = pdfReader.getPage(count)
    #     count +=1
    #     text += pageObj.extractText()
    #
    # print(text)
    x=1
    list = ["1"]

    String="https://d"
    for i in range(0, num_pages):
        PageObj = pdfReader.getPage(i)
        print("this is page " + str(i+1))
        Text = PageObj.extractText()
        # print(type(Text))
        ResSearch = re.search(String, Text)
        if ResSearch:
            print (ResSearch.group(0))
        if(ResSearch!=None):
            print(len(Text))

            for j in range(0, len(Text)):
                if(Text[j] == "h"):
                    # print("1")
                    if(Text[j]+Text[j+1]+Text[j+2]+Text[j+3]+Text[j+4]+Text[j+5]+Text[j+6]+Text[j+7]+Text[j+8]==String):
                        k = j+1
                        link = "h"
                        while(Text[k]!= " "):
                            if(Text[k]!="\n"):
                                temp = Text[k]
                                link = link+temp
                                # print(link)
                                k = k+1
                            else:
                                k=k+1
                        #print(type(link))
                        list.append(link)
                        # linklist = linklist+1
                        # print(linklist)
                        # list = ["Text[k]"]
                        # print("1")
                        # print(Text[j])
        print(ResSearch)

    print(len(list))
    print(list)
        # for x in list:
        # print(list)
    #
    # # tokens = word_tokenize(text)
    # # print(tokens)