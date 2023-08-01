from models.modpacks import ModPacks
from utils.repository import SQLAlchemyRepository


class ModPacksRepository(SQLAlchemyRepository):
    model = ModPacks
