#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from api.models import User, Portfolio, Asset
from api.models.Asset import Asset
from api.models.User import User
from api.models.Portfolio import Portfolio
from api.models.Relationship_PA import Relationship_PA
import api.models
from api.models.Base import Base

classes = {"Asset": Asset, "Portfolio": Portfolio, "User": User}

class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format('portfi_dev',
                                             'portfi',
                                             'localhost',
                                             'portfi'))

    def all(self, cls=None):
        """query on the current database session"""
        objs = self.__session.query(cls)
        return objs

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get_object(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls is User:
            objeto = self.__session.query(cls).filter_by(user_id=id).first()
            return objeto
        if cls is Asset:
            objeto = self.__session.query(cls).filter_by(asset_id=id).first()
            return objeto
        if cls is Portfolio:
            objeto = self.__session.query(cls).filter_by(portfolio_id=id).first()
            assetts_obj = self.__session.query(Relationship_PA).filter_by(portfolio_id=id)
            new_dict = {}
            for obj in assetts_obj:
                new_dict[obj.ticker] = obj.weight
            objeto.assets = new_dict
            objeto.performance = {}
            return objeto

        return None

    def get_ticker(self, ticker):
        try:
            objeto = self.__session.query(Asset).filter_by(ticker=ticker).first()
            return objeto
        except:
            return None


    def save_data(self, main_portfolio, user_obj):
        '''Save assets in MySQL table'''
        storage = DBStorage()
        storage.reload()
        for ticker, weight in main_portfolio.assets.items():
            relation_PA = Relationship_PA(main_portfolio.portfolio_id, ticker, weight)
            storage.new(relation_PA)
        relation_UP = Relationship_UP(main_portfolio.portfolio_id, user_obj.user_id)
        storage.new(relation_UP)
        storage.save()
        storage.close()
