from typing import Optional

from pydantic import BaseModel


class ModPacksSchema(BaseModel):
    id: int
    title: str
    author_id: int
    modpacks_author: Optional[str] = None
    short_description: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    save_file: Optional[str] = None
    mod_string: Optional[str] = None
    images: Optional[str] = None

    class Config:
        from_attributes = True


class ModPacksSchemaShort(BaseModel):
    id: int
    title: str
    author_id: int
    modpacks_author: Optional[str] = None
    short_description: Optional[str] = None
    logo: Optional[str] = None

    class Config:
        from_attributes = True


class ModPacksSchemaAdd(BaseModel):
    title: str
    author_id: int
    short_description: Optional[str] = None
    description: Optional[str] = None
    logo: Optional[str] = None
    save_file: Optional[str] = None
    mod_string: Optional[str] = None
    images: Optional[str] = None
