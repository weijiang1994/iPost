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
        self.engine = create_engine(f"sqlite:///{db_path}" + "?check_same_thread=False", echo=False, future=True)
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
    name = Column(String(512), default='', nullable=False)
    url = Column(TEXT, default='', nullable=False)
    headers = Column(TEXT, default='')
    query_param = Column(TEXT, default='')
    cookies = Column(TEXT, default='')
    collection_id = Column(INTEGER, ForeignKey('t_collections.id'))
    c_time = Column(DATETIME, default=datetime.datetime.now)

    collection = relationship('Collections', back_populates='request')
    history = relationship('History', back_populates='request')


class History(db.Model):
    __tablename__ = 't_history'

    id = Column(INTEGER, primary_key=True, autoincrement=True, nullable=False)
    url = Column(String(512), default='', nullable=False)
    request_id = Column(INTEGER, ForeignKey('t_request.id'))
    headers = Column(TEXT, default='')
    query_param = Column(TEXT, default='')
    c_time = Column(DATETIME, default=datetime.datetime.now)

    def __init__(self, url, request_id=None, headers='', query_param=''):
        self.url = url
        self.request_id = request_id
        self.headers = headers
        self.query_param = query_param

    def __repr__(self):
        return '%s -- %s' % (self.url, str(self.c_time))

    request = relationship('Request', back_populates='history')


# db.Model.metadata.create_all(db.engine, checkfirst=True)
#
# ws = WorkSpace(name='iPost', summary='I am superman', description='Just test')
# db.session.add(ws)
# db.session.commit()
