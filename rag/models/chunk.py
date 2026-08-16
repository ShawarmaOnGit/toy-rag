from pydantic import BaseModel, ConfigDict, computed_field, Field, field_validator

class Chunk(BaseModel):
    """
    This is the chunk with metadata that gets embedded, ranked, and cited. The records are 
    validated at creation.

    Records must be immutable and validated so that there is at least one character for each
    and pages start at 1.
    """
    model_config = ConfigDict(frozen=True)

    id: str
    text: str
    filename: str
    page: int = Field(gt=0)

    @computed_field
    @property
    def word_count(self) -> int:
        return len(self.text.split())

    @field_validator("id", "text", "filename")
    @classmethod
    def not_empty(cls, text: str) -> str:
        if not text.strip():
            raise ValueError("Text cannot be empty!")
        return text.strip()