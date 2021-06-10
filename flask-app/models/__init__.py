import models
from models.engine.db_storage import DBStorage
from models.User import User
#from models.Asset import Asset
from models.Portfolio import Portfolio


storage = DBStorage()
storage.reload()

### CREA INSTANCIAS DE USUARIO Y PORTFOLIO
# user_admin = models.User("Admin", "Admin", "Admin")
# models.storage.new(user_admin)
# portfolio = models.Portfolio("Default", 5, 0)
# bechmarck = models.Portfolio("Benchmark", 0, 0)
# portfolio.assets = {"VCSH":0.266, "HYG":0.0573, "LQD":0.0562, "AGG":0.0431, "VCIT":0.0413, "ANGL":0.0411, "ACWI":0.1041, "MOAT":0.0978, "EFA":0.07, "SPY":0.0609, "SPHQ":0.0453, "EEM":0.0379, "XLF":0.0156, "EMQQ":0.0123, "VB":0.0103, "CEF":0.0408}
# models.storage.new(portfolio)
# bechmarck.assets = { "ACWI": 0.5, "AGG": 0.5}
# models.storage.new(bechmarck)
# models.storage.save()

#PARA HACER LA POLULACION DE LA BASE DE DATOS LAS SIGUIENTE LINEAS DEBEN ESTAR COMENTADAS####
user_admin = storage.get_object(User, "8c62d1970-0548-4bc0-ba24-89452d05fd6a")
portfolio = storage.get_object(Portfolio, "337e9284-5113-4e8e-a52c-5277c65b9db0")
bechmarck = storage.get_object(Portfolio, "9c153db1-bbc7-4e43-8e9b-b30164f96fbb")
#models.portfolio.get_data_API()
#models.bechmarck.get_data_API()
#models.portfolio.add_performance(models.bechmarck)
############################################################################################