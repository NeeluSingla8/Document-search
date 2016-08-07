import rake
import operator
import io
import time
import unicodedata
import re

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

start_time = time.time()

def convert(fname):
    codec = 'utf-8'
    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, codec=codec, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)
    count = 0
    infile = file(fname, 'rb')
    for page in PDFPage.get_pages(infile):
        interpreter.process_page(page)
        count = count + 1
    infile.close()
    converter.close()
    text = output.getvalue()
    output.close
    return text, count 

pdf_string, page_no = convert('C:/USC stuff/MOSIS/Docs/Viacom18 - Project.pdf')
new_text1 = pdf_string.decode('utf-8', 'ignore')
new_text2 = unicodedata.normalize("NFKD", new_text1)
new_text3 = new_text2.encode('ascii', 'replace')

#print repr(pdf_string)
#print repr(new_text1)
#print repr(new_text2)
#print repr(new_text3)

# EXAMPLE ONE - SIMPLE
stoppath = "SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
min_chars = 5
max_words = 5
#if page_no <= 5:
#    min_freq = 2
if page_no <= 10:
    min_freq = 2
#elif page_no <= 50:
#    min_freq = 3
elif page_no <= 100:
    min_freq = 4
else:
    min_freq = 5
    
rake_object = rake.Rake(stoppath, min_chars, max_words, min_freq)
print "Rake call: (stoppath, %s, %s, %s )" % (min_chars, max_words, min_freq) 

keywords = rake_object.run(new_text3)

# 3. print results
#print("Keywords:", keywords)
#print("----------")

keywords1 = []
keywords2 = []
for j in range(0, len(keywords)):
    if re.search(r' \\x.. ', repr(keywords[j][0])) is not None:
        kstart = re.search(r' \\x.. ', repr(keywords[j][0])).start()
        kend =re.search(r' \\x.. ', repr(keywords[j][0])).end()
        start_phrase = repr(keywords[j][0])[1:kstart]
        end_phrase = repr(keywords[j][0])[kend:-1]
        keywords2.append(start_phrase)
        keywords2.append(end_phrase)
    else:
        keywords1.append(keywords[j][0])

keywords = keywords1 + keywords2
keyword_limit = min(len(keywords), 15)

for i in range(0, keyword_limit):
    keywords[i] = re.sub(r'\\x..', "", repr(keywords[i]))
    print keywords[i]

print ("--- %s seconds ---" % (time.time() - start_time))

