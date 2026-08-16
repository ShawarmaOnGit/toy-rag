from pydantic import BaseModel, computed_field, ConfigDict

class Chunk(BaseModel):
    model_config = ConfigDict(frozen=True)

    id: str
    text: str
    filename: str
    page: int

    @computed_field
    @property
    def word_count(self) -> int:
        return len(self.text.split())