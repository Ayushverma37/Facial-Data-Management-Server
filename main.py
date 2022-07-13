import psycopg2
import face_recognition
import zipfile
import tempfile
import sqlConnector
import faceRecognition
import numpy as np
from fastapi import FastAPI, File, UploadFile, Form

app = FastAPI()


@app.post("/search_faces/")
async def search_faces(k:str=Form(...), confidence_level:str=Form(...), file: UploadFile = File(..., description="An image file, possible containing multiple human faces.")):
   # getting encoding by calling the appropriate library class
   faceClass=faceRecognition.faceRecognition()
   known_face_encodings=faceClass.give_encoding(file.file)
   # if no face in img supplied
   if(len(known_face_encodings)<1):
      return {"status": "OK", "body": "no face found in the image supplied"}
   # typecasting into respective datatypes
   k=int(k)
   tolerance=1-float(confidence_level)
   # Connecting with postgress and fetching
   sql = sqlConnector.sqlConnector()
   records=sql.selectAll()
   flag=0
   # list of dictionaries to be returned as json
   arr=[]
   index=0
   for row in records:
      flag=0
      # calculating euclidean distance
      dist=faceClass.img_distance(known_face_encodings, np.array(row[6]))
      for i in range(len(dist)):
         # checking against tolerance value
         if(dist[i]<=tolerance):
            flag=1
            index=i
            break
      if(flag==1):
         dic={}
         # assigning values to the dictionary
         dic["id"]=row[0]
         dic["file_name"]=row[1]
         dic["person_name"]=row[2]
         dic["version"]=row[3]
         dic["location"]=row[4]
         dic["date"]=row[5]
         dic["distance"]=dist[index]
         # adding this to the list
         arr.append(dic)
   # sorting on the euclidean distance
   # lower the distance, more closer is the face match
   arr=sorted(arr, key = lambda i: (i["distance"]))
   finallist=[]
   # retreiving the top-k matches
   if(k<=len(arr)):
      for i in range(k):
         finallist.append(arr[i])
   else:
      for i in range(len(arr)):
         finallist.append(arr[i])
   # returning the json response
   return {"status": "OK", "body": {"matches": finallist}}



@app.post("/add_face/")
async def add_face(file: UploadFile = File(..., description="An image file having a single human face.")):
   # getting encoding by calling the appropriate library class
   faceClass=faceRecognition.faceRecognition()
   encoding=faceClass.give_encoding(file.file)
   # checking if the file contains a face
   if(len(encoding)>=1):
      # first face
      img_encoding = encoding[0]
      # connnecting with sql
      sql = sqlConnector.sqlConnector()
      sql.insertIntoTable(file.filename, str(img_encoding.tolist()))
      # returning the json response
      return {"status": "ok", "body": "elements inserted", "filename": file.filename}


@app.post("/add_faces_in_bulk/")
async def add_faces_in_bulk(file: UploadFile = File(..., description="A ZIP file containing multiple face images.")):
   # getting encoding by calling the appropriate library class
   faceClass=faceRecognition.faceRecognition()
   fileTemp = tempfile.TemporaryFile()
   fileTemp.write(file.file.read())
   zfile = zipfile.ZipFile(fileTemp, 'r')
   # iterating over the zip file
   for fileIterator in zfile.namelist():
      # checking if it is an image format or not
      if(fileIterator.endswith('.jpg') or fileIterator.endswith('.jpeg') or fileIterator.endswith('.png')):
         # getting encoding by calling the appropriate library class
         encoding=faceClass.give_encoding(zfile.open(fileIterator))
         # checking if the file contains a face
         if(len(encoding)>=1):
            img_encoding = encoding[0]
            # connnecting with sql
            sql=sqlConnector.sqlConnector()
            sql.insertIntoTable(fileIterator, str(img_encoding.tolist()))
   # returning the json response
   return {"status": "ok", "body": "elements inserted"}



@app.post("/get_face_info/")
async def get_face_info(api_key: str = Form(...), face_id: str = Form(...)):
   # connnecting with sql
   sql = sqlConnector.sqlConnector()
   records=sql.selectAgainstId(face_id)
   arr={}
   # if no rows
   if(len(records)==0):
      return {"status": "success", "body": "No entry in the table with this id"}
   else:
      # assigning the values to the dictionary
      arr["id"]=records[0][0]
      arr["file_name"]=records[0][1]
      arr["person_name"]=records[0][2]
      arr["version"]=records[0][3]
      arr["location"]=records[0][4]
      arr["date"]=records[0][5]
      # returning the json response
      return {"status": "success", "body": arr}




@app.post("/update_meta_data/")
async def update_meta_data(idTOBeUpdated: str = Form(...), person_name: str = Form(...), version: str = Form(...), location: str = Form(...), date: str = Form(...)):
   # connnecting with sql
   sql = sqlConnector.sqlConnector()
   sql.update_meta_data(idTOBeUpdated, person_name, version, location, date)
   # returning the json response
   return {"status": "success", "body": "metadataupdated"}

