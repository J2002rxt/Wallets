from fastapi import FastAPI, Body, Path, Query, Request, HTTPException, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import created_token, validate_token
from fastapi.security import HTTPBearer
from config.database import Session, engine, Base
from models.wallet import Wallet as WalletModel
from fastapi.encoders import jsonable_encoder

# Estamos creando una instancia de la clase FastAPI
app = FastAPI()
Base.metadata.create_all(bind=engine)

# Cambios a la documentacion
app.title = "MANSTYLE" 
app.version = "2.0.0"

class User(BaseModel):
    email: str
    password: str

class Wallet(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="wallet", min_length=5, max_length=30)
    overview: str = Field(default="Descripcion de la wallet", min_length=4, max_length=600)
    category: str = Field(default="Fibra de carbono", min_length=4, max_length=300)


class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "admin@gmail.com":
            raise HTTPException(status_code=401, detail="Invalid user")
        #return 

# Ahora crearemos nuestro primer endpoint 
@app.get("/", tags=['home']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Bienvenido a mi API </h1>")

@app.get("/wallets", tags=['wallets'], response_model=List[Wallet], status_code=200)#, dependencies=[Depends(JWTBearer())])
def get_wallets() -> List[Wallet]:
    db = Session()
    result = db.query(WalletModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

# Parte 2
@app.get("/wallet/{id}", tags=['wallet'], response_model=Wallet, status_code=200)
def get_wallet(id: int = Path(ge=1, le=2000)) -> Wallet:
    db = Session()
    result = db.query(WalletModel).filter(WalletModel.id == id).first()
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "wallet not found"}, status_code=404)
    return result

# Parte 3
@app.get("/wallets/", tags=['wallets'], response_model=List[Wallet])
def get_wallets_by_category(category: str = Query(min_length=3, max_length=15)) -> List[Wallet]:
    db = Session()
    result = db.query(WalletModel).filter(WalletModel.category == category).all()
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Wallet not found"}, status_code=404)
    return result

# Parte 4
@app.post("/wallets", tags=['wallets'], response_model=dict, status_code=201)
def create_wallet(wallet: Wallet) -> dict:
    db = Session()
    new_wallet = WalletModel(**wallet.model_dump())
    db.add(new_wallet)
    db.commit()
    return JSONResponse(content={"message": "wallet created successfully"}, status_code=201)

@app.put("/wallets/{id}", tags=['wallets'], response_model=dict, status_code=200)
def update_wallet(id: int, wallet: Wallet) -> dict:
    db = Session()
    result = db.query(WalletModel).filter(WalletModel.id == id).first()
    if not result:
        response = JSONResponse(content={"message": "Wallet not found"}, status_code=404)
    else:
        result.title = wallet.title
        result.overview = wallet.overview
        result.category = wallet.category
        db.commit()
        response = JSONResponse(content={"message": "Wallet updated successfully"}, status_code=200)
    return response

@app.delete("/wallets/{id}", tags=['wallets'], response_model=dict)
def delete_wallet(id: int) -> dict:
    db = Session()
    result = db.query(WalletModel).filter(WalletModel.id == id).first()
    if not result:
        response = JSONResponse(content={"message": "Wallet not found"}, status_code=404)
    else:
        db.delete(result)
        db.commit()
        response = JSONResponse(content={"message": "Wallet deleted successfully"})
    return response

@app.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User) -> dict:
    if user.email == "admin@gmail.com" and user.password == "admin":
        token = created_token(data=user.model_dump())
        return JSONResponse(content={"token": token}, 
                            status_code=200)
    else:
        return JSONResponse(content={"message": "Invalid credentials"},
                            status_code=401)