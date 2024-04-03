from typing import List
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Path, Query, Depends

from schemas.wallet import Wallet
from config.database import Session
from services.wallet import WalletService
from middlewares.jwt_bearer import JWTBearer
from models.wallet import Movie as MovieModel

movie_router = APIRouter()

@movie_router.get("/wallets", tags=['wallets'], response_model=List[Wallet], status_code=200)
def get_movies() -> List[Wallet]:
    db = Session()
    result = WalletService(db).get_wallets()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@movie_router.get("/wallets/{id}", tags=['wallets'], response_model=Wallet, status_code=200)
def get_movie(id: int = Path(ge=1, le=2000)) -> Wallet:
    db = Session()
    result = WalletService(db).get_wallet(id)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Wallet not found"}, status_code=404)
    return result

@movie_router.get("/movies/", tags=['movies'], response_model=List[Wallet])
def get_movies_by_category(category: str = Query(min_length=3, max_length=15)) -> List[Wallet]:
    db = Session()
    result = WalletService(db).get_wallets_by_category(category)
    if result:
        result = JSONResponse(content=jsonable_encoder(result), status_code=200)
    else:
        result = JSONResponse(content={"message": "Wallet not found"}, status_code=404)
    return result

@movie_router.post("/wallets", tags=['wallets'], response_model=dict, status_code=201)
def create_wallet(wallet: Wallet) -> dict:
    db = Session()
    WalletService(db).create_wallet(Wallet)
    return JSONResponse(content={"message": "Wallet created successfully"}, status_code=201)

@movie_router.put("/wallet/{id}", tags=['wallets'], response_model=dict, status_code=200)
def update_wallet(id: int, movie: Wallet) -> dict:
    db = Session()
    Wallet = WalletService(db).get_wallet(id)
    if not movie:
        response = JSONResponse(content={"message": "Wallet not found"}, status_code=404)
    else:
        WalletService(db).update_wallet(Wallet)
        response = JSONResponse(content={"message": "Wallet updated successfully"}, status_code=200)
    return response

@movie_router.delete("/wallets/{id}", tags=['wallets'], response_model=dict, dependencies=[Depends(JWTBearer())])
def delete_wallet(id: int) -> dict:
    db = Session()
    movie = WalletService(db).get_wallet(id)
    if not Wallet:
        response = JSONResponse(content={"message": "Wallet not found"}, status_code=404)
    else:
        WalletService(db).delete_wallet(Wallet)
        response = JSONResponse(content={"message": "Movie deleted successfully"})
    return response
