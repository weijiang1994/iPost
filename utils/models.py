"""
# coding:utf-8
@Time    : 2021/08/13
@Author  : jiangwei
@mail    : qq804022023@gmail.com
@File    : models.py
@Desc    : models
@Software: PyCharm
"""
from utils.common import Singleton, basedir
from sqlalchemy import create_engine, Column, String, INTEGER, TEXT, DATETIME, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
import datetime

db_path = basedir + '/resources/data/data.db'


class DBOperator(Singleton):
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{db_path}", echo=True, future=True)
        self.Model = declarative_base()
        self.session = sessionmaker(self.engine)()


db = DBOperator()


class WorkSpace(db.Model):
    __tablename__ = 't_workspace'

    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(512), default='', nullable=False)
    summary = Column(String(512), default='')
    description = Column(TEXT, default='')
    flag = Column(INTEGER, default=0, comment='0: normal 1:deleted')
    c_time = Column(DATETIME, default=datetime.datetime.now)

    collection = relationship('Collections', back_populates='workspace')


class Collections(db.Model):
    __tablename__ = 't_collections'

    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(512), default='', nullable=False)
    workspace_id = Column(INTEGER, ForeignKey('t_workspace.id'))
    tag = Column(String(512), default=0, nullable=False, comment='0: normal 1:deleted')
    c_time = Column(String(512), default=datetime.datetime.now)

    workspace = relationship('WorkSpace', back_populates='collection')
    request = relationship('Request', back_populates='collection')


class Request(db.Model):
    __tablename__ = 't_request'

    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    url = Column(String(512), default='', nullable=False)
    headers = Column(TEXT, default='')
    query_param = Column(TEXT, default='')
    cookies = Column(TEXT, default='')
    collection_id = Column(INTEGER, ForeignKey('t_collections.id'))
    c_time = Column(DATETIME, default=datetime.datetime.now)

    collection = relationship('Collections', back_populates='request')


db.Model.metadata.create_all(db.engine, checkfirst=True)

ws = WorkSpace(name='iPost', summary='I am superman', description='Just test')
db.session.add(ws)
db.session.commit()
