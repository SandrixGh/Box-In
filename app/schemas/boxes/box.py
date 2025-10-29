from pydantic import BaseModel, ConfigDict


class BoxBase(BaseModel):
    name: str
    description: str
    price: int

class BoxCreate(BoxBase):
    pass

class BoxUpdate(BoxBase):
    pass

class BoxRead(BoxBase):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: int