from config.database import Base 
from sqlalchemy import Column, Integer, String, Float

class Wallet(Base):
    __tablename__ = 'wallets'


    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    overview = Column(String, nullable=False)
    category = Column(String, nullable=False)
    
