from fastapi import FastAPI, Depends, HTTPException  
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm  
from pydantic import BaseModel  
import jwt  

app = FastAPI()  
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")  
SECRET_KEY = "your-secret-key"  

class User(BaseModel):  
    username: str  
    password: str  

users_db = {"admin": {"password": "secret"}}  

@app.post("/token")  
async def login(form_data: OAuth2PasswordRequestForm = Depends()):  
    user = users_db.get(form_data.username)  
    if not user or user["password"] != form_data.password:  
        raise HTTPException(status_code=400, detail="Incorrect credentials")  
    token = jwt.encode({"sub": form_data.username}, SECRET_KEY)  
    return {"access_token": token, "token_type": "bearer"}  

@app.post("/train")  
async def train_model(token: str = Depends(oauth2_scheme)):  
    try:  
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])  
        return {"status": "Training started"}  
    except jwt.PyJWTError:  
        raise HTTPException(status_code=401, detail="Invalid token")  