Submitter name: Ayush Verma

Roll No.: 2019csb1147

Course: CS305 Software Engineering

Assignment: 2

First of all refer to designDoc_Assignment2
==================================================================

1. What does this program do

An API service has been developed that perfoms "facial search" on a database of images.
The encoding of the image as well as the metadata related to the image is stored in the database.
I have used fastAPI for implementing the server API.
I have used postgresSQL database engine for storing these info.

Image containing face can be added as a single .jpg file or many image files zipped inside a zip folder.

The retrieval of top-k matches is very fast, as when I tested my program, it took less than 1 seconds for retreival although I have 5384 rows in my table.
'k' and 'confidence_level' are supplied as a paramter to the search_face function. 

all the functions corresponding to the post methods as specified by the template given by Sir.
One extra route is provided @app.post("/update_meta_data/"), this route is used for updating the metadata of the image in the table corresponding to supplied id.

==================================================================

2. A description of how this program works (i.e. its logic)

sqlConnector.py
This class is basically used to connect to the Postgres database and execute various select and insert functions on the SQL database. 
In my case, the table name was: imgtable
def __init__(self): This constructor specifies various parameters required for proper connection to the Postgres database. In my case, the password was set as "Ayush@37".
def insertIntoTable(self, fileName, encoding): This function is used to insert an entry into database.
def selectAll(self): This function is used to select all rows from the table.
def selectAgainstId(self, id): This function is used to fetch a row corresponding to id provided as a parameter.
def update_meta_data(self, id, person_name, version, location, date): This function is used to update the metadata field in the table corresponding to the id provided as a parameter.

faceRecognition.py
This class is basically used for any functions related to the “face recognition” library.
def give_encoding(self, img_file): This function returns encoding as a NumPy array for an image file provided as a parameter.
def img_distance(self, source, target): This function returns a list of distances between source and target image encodings by calculating the euclidean distance between them.

main.py
This is the main fast API server program file. 
It contains all the functions corresponding to the post methods as specified by the template given by Sir.
One extra route is provided @app.post("/update_meta_data/"), this route is used for updating the metadata of the image in the table corresponding to supplied id.

test_main.py
This file is basically used for unit testing the code.
assertion is done on response.status_code and response.json()
def test_1(): This test is used for testing the search_face route of the API.
def test_2(): This test is used for testing the add_face route of the API.
def test_3(): This test is used for testing the add_faces_in_bulk route of the API.
def test_4(): This test is used for testing the get_face_info route of the API.
def test_5(): This test is used for testing the update_meta_data route of the API.
==================================================================

3. How to compile and run this program

If you are running on Windows, make sure that you are on the python virtual environment, else face recognition library wont run.

Steps to download and open the project:
    Step1: download the zip folder and extract it.

Steps for unit-testing(and thus running) using powershell/terminal/vscode terminal
    Step1: cd into the "CS305-2019csb1147-2" folder on the appropriate terminal.
    Step2: type: coverage run -m pytest test_main.py
    Step3: for viewing the coverage report, type: coverage report -m


Step for just running the api server using powershell/terminal/vscode terminal
    Step1: type: uvicorn main:app --reload
    Step2: navigate to the proper endpoint by opening http://127.0.0.1:8000 on google chrome
    In google chrome you can then type http://127.0.0.1:8000/docs. Then run the required api route and supply with proper input parameters

Dependencies to be installed for running the code correctly:
    face-recognition library
    Pip install coverage
    FastApi dependencies
    Postgres dependencies
    Numpy array

If you are running on Windows, make sure that you are on the python virtual environment, else face recognition library wont run.

Solid Principles used 
    Single Responsibility Principle: Each class that I have implemented is responsible for handling its own functionality. For example: sqlConnector.py is responsible for connecting to the postgres and running queries of postgres in python, and the faceRecognition.py is responsible for functions related to the face_recognition library. Similarly, main.py and test_main.py handling their respective functionalities.
    Dependency Inversion Principle: Low level class (sqlConnector) closely related to hardware and High level class has been made.

NOTE: The code coverage is 97%. (Screenshot is attached in designDoc).
==================================================================

4. Provide a snapshot of a sample run

Snapshots are attached in designDoc.
