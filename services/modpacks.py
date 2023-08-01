from schemas.modpacks import ModPacksSchemaAdd
from utils.repository import AbstractRepository


class ModPacksService:
    def __init__(self, modpacks_repo: AbstractRepository):
        self.modpacks_repo: AbstractRepository = modpacks_repo()

    async def add_modpack(self, modpack: ModPacksSchemaAdd):
        modpacks_dict = modpack.model_dump()
        modpack_id = await self.modpacks_repo.add_one(modpacks_dict)
        return modpack_id

    async def get_modpacks(self):
        modpacks = await self.modpacks_repo.get_list()
        return modpacks

    async def get_modpack(self, item_id):
        modpacks = await self.modpacks_repo.get_item_by_id(item_id)
        return modpacks
