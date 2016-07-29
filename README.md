ETL MANAGEMENT TOOLKIT


Seminar


Submitted in Partial fulfillment of the requirements 
For Fourth Year Sem VII Examination


BY


                                          GAURANGI RAUL
KRITESH BHIMANI
SAGAR MEISHERI



                                          Under the guidance of

                                              Mrs. JYOTI RAO




DEPARTMENT OF COMPUTER ENGINEERING
K. J. SOMAIYA COLLEGE OF ENGINEERING, MUMBAI
UNIVERSITY OF MUMBAI


                                                2011-2012

 

Seminar entitled:  	 ETL MANAGEMENT TOOLKIT



Submitted by: 		GAURANGI RAUL (0811030)
KRITESH BHIMANI (0811045)
                                     SAGAR MEISHERI (0811088)


in Partial fulfillment of the for Fourth Year Sem VII Examination
is approved.



Mentor						Examiners


Mrs. JYOTI  RAO				------------------

							------------------
								
							------------------
							

                    
               ------------------                               					

					
Head of Department					Principal
Date: 












CONTENTS
Chapter 1
ABSTRACT…………………………………………………………………….5
Chapter 2
INTRODUCTION……………………………………………………………...6
Chapter 3
AIMS AND OBJECTIVES……………………………………………………7
Chapter 4
LITERATURE SURVEY……………………………………………………..8
Chapter 5
EXISTING SYSTEMS………………………………………………………..9
Chapter 6
PROBLEM DEFINITION…………………………………………………….10
Chapter 7
SCOPE…………………………………………………………………….…..11
Chapter 8
PROPOSED SYSTEM………………………………………………………12
Chapter 9
METHODOLOGY…………………………………………………………….13
Chapter 10
ANALYSIS…………………………………………………………………….14


Chapter 11
HARDWARE AND SOFTWARE PLATFORM REQUIREMENTS, PROGRAMMING TOOLS…………………………………………………………………….…..20
Chapter 12
DESIGN DETAILS………………………………………………………......21
Chapter 13
CURRENT STATUS OF THE PROJECT……………………………......22
Chapter 14
IMPLEMENTATION PLAN FOR EIGHTH SEMESTER………………..23
Chapter 15
REFERENCES……………………………………………………………	…24 
1. ABSTRACT

Data warehousing helps to provide information on the techniques involved in designing, building, maintaining and retrieving information, from a data warehouse. A data warehouse is premeditated and produced to support the decision-making process in an organization. The data that is obtained from the production databases are copied in the data warehouse, so that queries can be answered, without hindering the consistency of the production systems.

As the amount of data keeps on increasing, it becomes more difficult to handle the data. The primary reason for that is because of its heterogeneity.
The various types of heterogeneity that exists are as follows:
•	Technical Heterogeneity
•	Data Model Heterogeneity
•	Semantic Heterogeneity

In the past decade, research works in heterogeneous database integration have established a good and solid framework to alleviate this task. However, there are still works need to be accomplished to bring these achievements to be easily implemented and integrated to Internet applications.









 
2.INTRODUCTION

The term ETL which stands for extract, transform, and load is a three-stage process in database usage and data warehousing. It enables integration and analysis of the data stored in different databases and heterogeneous formats. After it is collected from multiple sources (extraction), the data is reformatted and cleansed for operational needs (transformation). Finally, it is loaded into a target database, data warehouse or a data mart to be analysed. Most of numerous extraction and transformation tools also enable loading of the data into the end target. Except for data warehousing and business intelligence, ETL Tools can also be used to move data from one operational system to another.
XML has evolved from a document markup language to a widely-used format for exchange of structured and semistructured data, managing large amounts of XML data has become increasingly important. A number of companies, including both established database vendors and startups, have recently announced new XML database systems or new XML functionality integrated into existing database systems.
The success and broad use of XML mainly derives from it being platform independent, text based, straightforward, easy to understand, human readable and user defined.
Each ETL process for the XML processing task comes with its own challenges and requires its own techniques.
 

3.AIMS AND OBJECTIVES
ETL tools are designed to save time and money by eliminating the need of ‘hand-coding' when a new data warehouse is developed. They are also used to facilitate the work of the database administrators who connect different branches of databases as well as integrate or change the existing databases. 
The main purpose of the ETL tool is: 
•	Extraction of all types of data from various colleges
•	Data transformation (Overcoming schema conflicts)
•	Synchronization and cleansing of the data 
•	Loading the data into data warehouse. 
We intend to design an ETL tool which will overcome the heterogeneity problems faced during data extraction.
Thus we are employing the XML based data integration solution which will not only extract the relevant data from various sources but also map this data according to the needs of database administrators.
The ETL tool provides the database administrators to map the data according to their requirements.














4.LITERATURE SURVEY

1.	XML-Based Heterogeneous Database Integration For Data [1] Warehouse Creation, Frank S.C. Tseng1:

This paper helped us in understanding the various schema conflicts that arise in heterogeneous database integration and how XML can be used to overcome those conflicts.The various schema conflicts that arise during data integration are as follows:
a)	Table-to-table conflicts: Arises due to different table names
b)	Value-to-value conflics: Arises due to different values used for the same entity of data
c)	Attribute-to-attribute conflicts: Arises due to different column names of related data


2.	http://etl-tools.info/en/examples/xml-etl-processing.htm
Most XML ETL processing tasks tend to yield to one of the two ways the data is interpreted and represented: 

•	Event XML model: is a way to interpret XML as a series of events. Each incoming XML data string is treated as a separate entity - an event. In the XML event approach each of those events is converted to a record in a data flow, where each tag and attribute value is stored in a separate field. This model can be set up quickly, it works with every kind of XML document and the elements can be adjusted as needed. However, the event model does not provide the same level of support for XML Schema, in many cases this model ignores some parts of the document which may result in incomplete data. The event model is a simple way of interpreting XML strings, and one that does not involve great effort to set up. 



•	 Full XML parse processing model - at the time of reading the XML document, an ETL tool component knows the exact document structure and parses it accordingly. It requires additional work effort to be done in the preliminary setup phase, however this approach increases performance and ensures the proper mapping of all values and nullable fields. Another outcome of the investment in this approach is a reduced need for populating downstream components as it is far more error proof. 
The Full Object model representation is more sophisticated, the most powerful and useful choice when working with complex XML schemas.






 



5.EXISTING SYSTEM

The colleges need to send the students’ results to the University for its approval but their data are not compatible as they use different DBMS.
So the university cannot directly store the data sent by colleges into its own DBMS and also the colleges cannot store the data sent by the university directly into its own DBMS. 
Generally, the hard copies of results are sent from both the ends which are scanned and stored. Then the data can be entered manually to store the results into its DBMS. This entire process becomes cumbersome since there is no automation involved.
The various existing ETL tools available in the market do not address this problem efficiently as they are usually problem-specific. Also the ETL tools are very costly.









 


6.PROBLEM  DEFINITION

University has many colleges under it. University needs to keep a record of the students enrolled in these colleges along with their results. All these colleges use different DBMS to store their data while the university has its own different DBMS. Each college creates a local schema describing the data as per its convenience, whereas the university has to maintain a global schema by mapping the local schemas of these colleges. To overcome this heterogeneity problem faced during the integration of data, the University will need an ETL Management Toolkit.  










 

7.SCOPE

University will maintain a data warehouse which will contain the information about the current students. Whenever new students are enrolled by the colleges the university needs to add the student data to its pre-existing data warehouse. Every academic semester, all the colleges will upload its students results on the University website. The university will also need to update the student records by extracting the relevant data, transforming and mapping it with its database and loading it into the warehouse. The University will perform analysis on this data. 















 


8.PROPOSED SYSTEM

We intend to develop an ETL Management Toolkit for the University to enable integration of data from various colleges.

We will use the XML approach to achieve this task.





 


WHY XML ??
	Platform independent 
	Text based 
	Straight forward and easy to understand 
	User defined 
	Can be easily used over the Internet
	Can access XML using JDBC also


9.METHODOLOGY

•	The aim of our ETL tool is to integrate data from various XML files and load it into the University server as per their requirement.

•	The ETL tool will overcome the schema conflicts which may arise as data in different colleges is stored in different formats.

•	Every college will upload its relational database by logging in to the University website. These relational databases will be then converted into XML files. 

•	Then the XML source files are moved from the web server to the ETL server.

•	The ETL tool will process each of the XML files individually :
o	Parse the XML file using JAVA
o	Define the mapping function to resolve the schema conflicts
o	Apply transformations as required by the warehouse manager

 



10.ANALYSIS

10.1 SOFTWARE PROJECT MANAGEMENT PLAN
10.1.1 Roles and Responsibilities

In order to complete the project successfully, the various tasks are assigned amongst the group members according to their ability. Each member should perform the given task efficiently. The members should give proper design for the code, based on which the functions have to be performed:


Following table shows the roles and responsibilities of the each member:
Roles
		Name
	Responsibilities

Team Leader
	Sagar Meisheri	Design generation
Integration of modules

Project Manager	Gaurangi Raul	Evaluation of codes
Management of the database
Project Analyser	Kritesh Bhimani	Analysis
Requirement gathering & Testing



10.1..2 Timetable
Tasks		Description	Days allotted	Start date	End date
Requirement gathering	Collection of information and
Analysis of various books and reference papers.	25	July 2011	Aug 2011
Algorithm study	On ETL processing using JDBC	15	Aug 2011	Sept 2011
Prototype Development	ETL Processing for XML files	25	Sept 2011	Oct 2011
	Applying Transformations	10	Sept 2011	Oct 2011
Designing of graphics user interface	Using java	20	Oct 2012	Nov 2012
Testing	Testing of ETL Tool Kit	10	Nov 2011	Nov 2011
Conversion of relational databases into XML format	Development of program in JAVA	25	Jan 2012	Feb 2012
Uploading of XML files	Sending files to the ETL sever 	25	Feb 2012	Mar 2012
Testing of complete system	Testing various modules	15	Apr 2012	May2012

10.2 SOFTWARE REQUIREMENT SPECIFICATION
10.2.1 System proposed:
	System developed will be simple, easy to use, and efficient.
10.2.2 Compatibility:
	The complete system will work on all Windows Vista and XP configurations.
	The microphone and speakers of minimal configuration can be employed
	easily.
 
 
10.3  SOFTWARE DESIGN DOCUMENT
10.3.1 Use Case Diagram:


 




10.3.2 Activity Diagram:
ETL MANAGEMENT TOOL-KIT
 




10.3.3 Sequence Diagrams:
 


 
11. HARDWARE AND SOFTWARE REQUIREMENTS

11.1 HARDWARE   REQUIREMENTS:
	Desktop personal computer
	512 MB RAM
	Connection to the Internet

11.2 SOFTWARE   REQUIREMENTS: 
	MS SQL
	JAVA PROGRAMMING LANGUAGE(JCreator)
	MS OFFICE
	XML


 
12.DESIGN DETAILS

 

 

 

•	The user interface for the program has been implemented using the features of Java swing and awt packages.
•	The main window will help the user to start the ETL process.
•	The extraction window will allow the user to select the xml files of three different colleges. We have used the event-xml model to extract the data from the xml files. 
•	The transformation window will enable the user to map all the attributes as per the requirements of the final database.
•	The loading window will display that the data has been successfully loaded into the target database.




13.CURRENT STATUS OF THE PROJECT

•	 Successfully parsed the XML files of the 3 different colleges containing student results.

•	The extracted data contains various schema heterogeneities

•	Mapping is done by the database administrator according to need of the final database.

•	A transformation GUI aids the mapping process for the administrator.

•	The transformed data is finally loaded into university database.
 
14.IMPLEMENTATION PLANS FOR THE NEXT SEMESTER

•	Conversion of relational databases into XML format:
o	Since we are employing XML methodology to integrate heterogeneous data from different sources, it is necessary to convert the different relational data into XML format first. We intend to apply the ETL process on these XML files later on.  

•	Easy uploading of  XML files in the ETL server:
o	After the relational data is converted into XML format, the colleges must be able to upload the XML files onto the ETL server directly using LAN, FTP, etc.

•	Analysis :
o	The University can analyse the results of various colleges.



 
15.REFERENCES

Books:
1.	The data warehouse ETL toolkit: practical techniques for extracting, cleaning, conforming, and delivering data by Ralph Kimball, Joe Caserta.
White papers: 
[1]XML-Based Heterogeneous Database Integration For Data Warehouse Creation, Frank S.C. Tseng1
            [2]XML and Relational Database Integration, Stephen A. Broadsky

Websites:
1.	 http://etl-tools.info/en/examples/xml-etl-processing.htm
2.	en.wikipedia.org

