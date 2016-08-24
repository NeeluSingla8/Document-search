import sys
import rake
import re
import mysql.connector
import os
from googleapiclient.discovery import build
from PyPDF2 import PdfFileWriter, PdfFileReader
import datetime
import time

my_api_key = "AIzaSyBX7n9j5SfCBxOLtWGsE4SwmMMdQOD7sdY"
my_cse_id = "001888581548700543885:hcpwduckiys"

if __name__=="__main__":
	config = {
        'host': 'localhost',
        'port': 3306,
        'database': 'testdb',
        'user': 'root',
        'password': 'Backspacebar@1',
        'charset': 'utf8',
        'use_unicode': True,
        'get_warnings': True,
    }
	filename=sys.argv[1]
	stopwordfile=sys.argv[2]
	cnx = mysql.connector.connect(**config)
	cursor = cnx.cursor()
	now = datetime.datetime.now()
	print(now.strftime("%Y-%m-%d %H:%M:%S"))
	date = now.strftime("%Y-%m-%d %H:%M:%S")
	while('true'):
		for file in os.listdir(filename):
			print(file)
			
			rake_object = rake.Rake(stopwordfile, 5, 5, 2)
			path = filename + '\\' + file
			print(path)
			watermark = PdfFileReader(open(path, "rb"))
			pdfdata=""
			total=0
			counter=0
			for j in range(0, watermark.getNumPages()):
				pdfdata=pdfdata+watermark.getPage(j).extractText()
			print(len(pdfdata))
			keywords = rake_object.run(pdfdata)
			
			keyword_limit = min(len(keywords), 5)
			keywordAllData=""
			i = keyword_limit
			while i > 0:
				print(keywords[i][0])
				if not re.match(r'.*[\%\$\^\*\@\!\-\(\)\:\;\'\"\{\}\[\]].*', keywords[i][0]) :
					keywordAllData=keywordAllData+"\""+keywords[i][0] +"\","
				i = i -1
			print(keywordAllData)
			sql = "INSERT INTO FILE_METADATA(FILENAME,DATE, keywords) VALUES ('%s' , '%s' , '%s')" % (file, date , keywordAllData)
			cursor.execute(sql)
			id = cursor.lastrowid
			print(id)
			cnx.commit()
			service = build("customsearch", "v1", developerKey=my_api_key)
			res = service.cse().list(q=keywordAllData, cx=my_cse_id, filter='0').execute()
			print('Top 10 google search urls are:-')
			if (len(res) == 6):
				for result in res['items']:
					print(result['link'])
					sql = "INSERT INTO URL(FILE_ID,URL_NAME) VALUES (%s , '%s')" % (id,result['link'])
					cursor.execute(sql)
					
					cnx.commit()
					counter=counter+1
					if ("github.com/NeeluSingla8" in result['link']):
						total = total +1
			if (counter != 0) :
				print("precison is :- " + str((total/counter)))
				print("recall is :- " + str((total/max(total,counter))))
			else :
				print("precison is :- 0")
				print("recall is :- 0")
		print("going to run after 1 day")
		time.sleep(24*3600)
