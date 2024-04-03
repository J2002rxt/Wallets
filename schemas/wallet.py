from pydantic import BaseModel, Field
from typing import Optional

class Wallet(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Mi wallet", min_length=5, max_length=30)
    overview: str = Field(default="Descripcion de la wallet", min_length=5, max_length=300)
    category: str = Field(default="Fibra de carbono", min_length=5, max_length=40)
    
    # Configuracion de la documentacion
    class Config:
        model_config = {
        "json_schema_extra": {
                "examples": [
                    {
                        "id": 1,
                        "title": "Mi wallet",
                        "overview": "Descripcion de la wallet",
                        "category": "Fibra de carbono"
                    }
                ]
            }
        }
