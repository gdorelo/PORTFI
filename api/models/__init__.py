from api.models.engine.db_storage import DBStorage
from api.models.User import User
from api.models.Asset import Asset
from api.models.Portfolio import Portfolio
import api.models as models

storage = DBStorage()
storage.reload()

user_admin = storage.get_object(User, "c62d1970-0548-4bc0-ba24-89452d05fd6a")
portfolio = storage.get_object(Portfolio, "337e9284-5113-4e8e-a52c-5277c65b9db0")
bechmarck = storage.get_object(Portfolio, "9c153db1-bbc7-4e43-8e9b-b30164f96fbb")
models.portfolio.get_data_API()
models.bechmarck.get_data_API()
models.portfolio.add_performance(models.bechmarck)
