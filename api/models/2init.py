# #!/usr/bin/python3
# from models.User import User
# from models.Asset import Asset
# from models.Portfolio import Portfolio
# from models.engine.db_storage import DBStorage

# storage = DBStorage()
# storage.reload()


# portfolio = Portfolio("Default", 5, 10000)
# portfolio.assets = {"VCSH":0.5, "HYG":0.1}
#portfolio.assets = {"VCSH":0.266, "HYG":0.0573, "LQD":0.0562, "AGG":0.0431, "VCIT":0.0413, "ANGL":0.0411, "ACWI":0.1041, "MOAT":0.0978, "EFA":0.07, "SPY":0.0609, "SPHQ":0.0453, "EEM":0.0379, "XLF":0.0156, "EMQQ":0.0123, "VB":0.0103, "CEF":0.0408}
#storage.new(portfolio)

# bechmarck = Portfolio("Bechmarks", 0, 0)
# bechmarck.assets = { "ACWI": 0.5, "AGG": 0.5}
#storage.new(bechmarck)

#user_admin = User("Admin", "Admin", "Admin")
#storage.new(user_admin)
#storage.save()



#SECCION DONDE CREA EL OBJETO SEGUN LA BASE DE DATOS

# user_admin = storage.get_object(User, "c62d1970-0548-4bc0-ba24-89452d05fd6a")
# print(user_admin)
# asset = storage.get_object(Asset, "20")
# print(asset)
# portfolio = storage.get_object(Portfolio, "337e9284-5113-4e8e-a52c-5277c65b9db0")
# print(portfolio)
# bechmarck = storage.get_object(Portfolio, "9c153db1-bbc7-4e43-8e9b-b30164f96fbb")