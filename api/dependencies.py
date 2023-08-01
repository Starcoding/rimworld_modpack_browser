from repositories.modpacks import ModPacksRepository
from repositories.users import UsersRepository
from services.modpacks import ModPacksService
from services.users import UsersService


def modpacks_service():
    return ModPacksService(ModPacksRepository)


def users_service():
    return UsersService(UsersRepository)
