from fastapi import FastAPI
from bson import ObjectId
from config.db import db
from typing import  List
from models.products import Products

app= FastAPI()

@app.get('/api/v1/products',  response_description="List all products", response_model=List[Products])
async def get_all_products(page:int=1, featured:bool= None, company:str =None, name:str =None):
    #featured, company, name, sort, fields
    query = {}
    
    if featured:
        query['featured'] = featured
 
    if company:
        query['company'] = company

    if name:
        query['name'] = "{ $regex: name , $options: 'i' }"
    

    limit: int = 10
    skip= (int(page) - 1) * limit
    products= await db["products"].find(query,skip= skip, limit= limit).to_list(1000)
    return products