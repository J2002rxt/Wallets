from schemas.wallet import Movie
from models.wallet import Movie as WalletModel

class MovieService():
    def __init__(self, db):
        self.db = db

    def get_movies(self):
        return self.db.query(WalletModel).all()

    def get_movie(self, id:int):
        return self.db.query(WalletModel).filter(WalletModel.id == id).first()
    
    def get_movies_by_category(self, category:str):
        return self.db.query(WalletModel).filter(WalletModel.category == category).all()
    
    def create_movie(self, movie:Movie):
        new_movie = WalletModel(**movie.model_dump())
        self.db.add(new_movie)
        self.db.commit()

    def update_movie(self, movie: WalletModel, data:Movie):
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        self.db.commit()

    def delete_movie(self, movie: WalletModel):
        self.db.delete(movie)
        self.db.commit()