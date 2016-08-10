import glob, os
import io
import unicodedata
import re
import rake

from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from googleapiclient.discovery import build

#set Google API key and Custom Search Engine ID
my_api_key = "Your API key"
my_cse_id = "Your CSE ID"

#initialize the stopwords list
stoppath = "SmartStoplist.txt"

#set directory for the files
os.chdir("C:\USC stuff\MOSIS\Test_Files")

#module to convert pdf to text
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

#module to implement rake
def rake_call(final_string, page_no):
    min_chars = 5
    max_words = 5
    if page_no <= 10:
        min_freq = 2
    elif page_no <= 30:
        min_freq = 3
    elif page_no <= 100:
        min_freq = 4
    else:
        min_freq = 8
    
    rake_object = rake.Rake(stoppath, min_chars, max_words, min_freq)
#   print "Rake call: (stoppath, %s, %s, %s )" % (min_chars, max_words, min_freq) 
    keywords = rake_object.run(final_string)
    return post_process(keywords)

#module to remove unicode characters if any
def post_process(keywords):
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
    keyword_string = ""
    for i in range(0, keyword_limit):
        keywords[i] = re.sub(r'\\x..', "", repr(keywords[i]))
        keyword_string = keyword_string + keywords[i] + " "
    keyword_string = keyword_string.replace("'", '"')
    return keyword_string
    
#module to process unicode text to string text
def preprocess(infile):
    pdf_string, page_no = convert(infile)
    decoded_string = pdf_string.decode('utf-8', 'ignore')
    normalized_string = unicodedata.normalize("NFKD", decoded_string)
    final_string = normalized_string.encode('ascii', 'replace')
    return rake_call(final_string, page_no)

#module to perform google search
def google_search(search_term, api_key, cse_id):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id).execute()
    total_results = int(res['searchInformation']['totalResults'])
    if total_results == 0:
        return ""
    else:
        return res['items']

for infile in glob.glob("*.pdf"):
    print "Filename: ", infile
    keyword_string = preprocess(infile)
    print "Keywords: ", keyword_string
    results = google_search(keyword_string, my_api_key, my_cse_id)
    if results == "":
        print "No results"
    else:
        print "Search Results:"
        for result in results:
            print(result['link'])
    print "-------------------------------------------------------------"


    
