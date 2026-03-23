from fastapi import FastAPI, Body
from pydantic import BaseModel
import json

app = FastAPI()

# class item(BaseModel):
#     my_string: str

LoudList = []

# get
# www.google.com//
# 127.0.0.1/
@app.get("/")
def get_root():
    """
    Get Root

    This is the root of the API, this is a smoke-check to check if the app actually runs.
    """
    return "Hello World"

@app.get("/loudlist")
def get_loudlist():
    """
    Get LoudList
    
    A simple get request endpoint, to return a list of values from the client.
    """
    return json.dumps({"LoudList": LoudList})

# put
@app.put("/loudlist/{list_index}")
def update_list(list_index: int, wrapper: str=Body()):
    """
    Update LoudList
    
    A simple put request endpoint, to update a list value from the client.
    """
    LoudList[list_index] = wrapper
    return json.dumps({"LoudList": LoudList})

# post
@app.post("/")
def post_root(wrapper: str=Body()):
    """
    Post Root
    
    A simple post request endpoint, to accept a value from the client
    """
    LoudList.append(wrapper.upper())
    return json.dumps({"Greeting": wrapper.upper()})

# patch

# delete
@app.delete("/benslist")
def delete_benslist():
    """
    Delete Ben's List
    
    A simple delete request endpoint, to clear the list of values from the client.
    """
    global LoudList
    LoudList = []
    return json.dumps({"LoudList": LoudList})

# head
# options
# connect