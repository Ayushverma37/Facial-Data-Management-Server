from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


# This test is used for testing the search_face route of the API
def test_1():
    with open("Atal_Bihari_Vajpayee_0018.jpg", "rb") as f:
        
        response = client.post(
                "http://127.0.0.1:8000/search_faces/",
                data={
                    "k": 3,
                    "confidence_level": 0.4
                },
                files={"file": ("img", f, "image/jpeg")}
                
        )
        
        # assertion is done on response.status_code and response.json()
        assert response.status_code == 200
        assert response.json()=={
  "status": "OK",
  "body": {
    "matches": [
      {
        "id": 1008,
        "file_name": "Atal_Bihari_Vajpayee_0018.jpg",
        "person_name": None,
        "version": None,
        "location": None,
        "date": None,
        "distance": 0
      },
      {
        "id": 1013,
        "file_name": "Atal_Bihari_Vajpayee_0023.jpg",
        "person_name": None,
        "version": None,
        "location": None,
        "date": None,
        "distance": 0.3212965238882343
      },
      {
        "id": 1012,
        "file_name": "Atal_Bihari_Vajpayee_0022.jpg",
        "person_name": None,
        "version": None,
        "location": None,
        "date": None,
        "distance": 0.3372265074960653
      }
    ]
  }
}
        
# This test is used for testing the add_face route of the API        
def test_2():
    with open("modi.jpg", "rb") as f:
        
        response = client.post(
                "http://127.0.0.1:8000/add_face/",
                files={"file": ("modi.jpg", f, "image/jpeg")}
                
        )
        
        # assertion is done on response.status_code and response.json()
        assert response.status_code == 200
        assert response.json()=={
  "status": "ok",
  "body": "elements inserted",
  "filename": "modi.jpg"
}
        
     
# This test is used for testing the add_faces_in_bulk route of the API
def test_3():
    with open("testCase3.zip", "rb") as f:
        
        response = client.post(
                "http://127.0.0.1:8000/add_faces_in_bulk/",
                files={"file": ("testCase3.zip", f, "application/x-zip-compressed")}
                
        )
        
        # assertion is done on response.status_code and response.json()
        assert response.status_code == 200
        assert response.json()=={
  "status": "ok",
  "body": "elements inserted"
}


# This test is used for testing the get_face_info route of the API
def test_4():
        response = client.post(
                "http://127.0.0.1:8000/get_face_info/",
                data={
                    "api_key": 1,
                    "face_id": 100
                }
        )
        
        # assertion is done on response.status_code and response.json()
        assert response.status_code == 200
        assert response.json()== {
  "status": "success",
  "body": {
    "id": 100,
    "file_name": "Afton_Smith_0001.jpg",
    "person_name": None,
    "version": None,
    "location": None,
    "date": None
  }
}
        
        
# This test is used for testing the update_meta_data route of the API        
def test_5():
        response = client.post(
                "http://127.0.0.1:8000/update_meta_data/",
                data={
                    "idTOBeUpdated": 3000,
                    "person_name": "Ayush",
                    "version": 1,
                    "location": "Ropar",
                    "date": "07/11/1999",
                }
        )
        
        # assertion is done on response.status_code and response.json()
        assert response.status_code == 200
        assert response.json()=={
  "status": "success",
  "body": "metadataupdated"
}
        
       
     

      
        
        

    
