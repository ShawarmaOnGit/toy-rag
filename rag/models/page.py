from pydantic import BaseModel, ConfigDict, Field

class Page(BaseModel):
    model_config = ConfigDict(frozen=True)

    text: str
    filename: str
    page: int = Field(gt=0)