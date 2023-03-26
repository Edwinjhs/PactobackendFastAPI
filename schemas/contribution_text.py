from pydantic import BaseModel


class ContributionText(BaseModel):
    text: str
    contribution_id: int

    class Config:
        orm_mode=True
        schema_extra = {
            "example": {
                "text": "mi contribucion en conocimiento..., -> contribution_id=1Conocimiento,2Buenas Practicas,3Casos Exitosos,4Ninguna Contribucion",
                "contribution_id": 1
            }
        }