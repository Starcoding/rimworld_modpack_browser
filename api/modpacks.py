from typing import Annotated

from fastapi import APIRouter, Depends
from starlette import status

from api.dependencies import modpacks_service
from schemas.modpacks import ModPacksSchema, ModPacksSchemaAdd, ModPacksSchemaShort
from services.modpacks import ModPacksService

router = APIRouter(
    prefix="/modpacks",
    tags=["ModPacks"],
)


@router.post("")
async def add_modpack(
    modpack: ModPacksSchemaAdd,
    modpacks_service: Annotated[ModPacksService, Depends(modpacks_service)],
):
    modpack_id = await modpacks_service.add_modpack(modpack)
    return {"modpack_id": modpack_id}


@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[ModPacksSchemaShort],
)
async def get_modpacks(
    modpacks_service: Annotated[ModPacksService, Depends(modpacks_service)],
):
    modpacks = await modpacks_service.get_modpacks()
    return modpacks


@router.get(
    "/{item_id}",
    status_code=status.HTTP_200_OK,
    response_model=ModPacksSchema,
)
async def get_modpack(
    item_id: int,
    modpacks_service: Annotated[ModPacksService, Depends(modpacks_service)],
):
    modpack = await modpacks_service.get_modpack(item_id)
    return modpack
