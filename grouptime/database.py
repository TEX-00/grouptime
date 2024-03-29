# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

#データベースはローカルのsqliteを使用
database_file=os.path.join(os.path.abspath(os.path.dirname(__file__)),'groups.db')
engine = create_engine('sqlite:///'+database_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

Base = declarative_base()
Base.query= db_session.query_property()

#初期化
def init_db():
    import grouptime.models
    Base.metadata.create_all(bind=engine)