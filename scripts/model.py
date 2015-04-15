from os.path import join as pjoin

from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Float, String, Column, Table, \
    ForeignKey, Boolean, create_engine, orm

from itertools import chain

import json


ROOT_DIR = "."

DB_DIR = "data"
DB_NAME = "all_data.db"
DB_PATH = pjoin(ROOT_DIR, DB_DIR, DB_NAME)

VERBOSE = True

DeclBase = declarative_base()


class ParseableMixin:
    DEFAULT_MAPPING = {
        'ts': ('timestamp', float)
    }

    @classmethod
    def parse(cls, s):
        d = json.loads(s)
        kwargs = {key : f(d[table_key]) for key, (table_key, f)
                  in chain(cls.mapping.items(), cls.DEFAULT_MAPPING.items())}
        return cls(**kwargs)

class PrintableMixin:
    def __repr__(self):
        fmt = "{}({})"
        name = self.__class__.__name__
        attrs = ", ".join(["{}={}".format(key, repr(value)) for key, value in
                           self.__dict__.items() if key[0] != '_'])

        return fmt.format(name, attrs)


class DeclTableBase(ParseableMixin, PrintableMixin):
    pass

class ActivtyLevel(DeclBase, DeclTableBase):
    __tablename__ = 'activitylevel'
    id = Column(Integer, primary_key=True)

    level = Column(String)
    ts = Column(Float)

    mapping = {
        'level': ('activityLevel', lambda x: x)
    }

class Proximity(DeclBase, DeclTableBase):
    __tablename__ = "proximity"
    id = Column(Integer, primary_key=True)

    is_close = Column(Boolean)
    ts = Column(Float)

    mapping = {
        'is_close': ('distance', lambda x: x == 0)
    }

class Acceleration(DeclBase, DeclTableBase):
    __tablename__ = 'acceleration'
    id = Column(Integer, primary_key=True)

    x = Column(Float)
    y = Column(Float)
    z = Column(Float)

    ts = Column(Float)

    mapping = {k: (k, float) for k in ('x', 'y', 'z')}

class ScreenOn(DeclBase, DeclTableBase):
    __tablename__ = 'screenons'
    id = Column(Integer, primary_key=True)

    is_on = Column(Boolean)
    ts = Column(Float)

    mapping = {
        'is_on': ('screenOn', bool),
    }

class Battery(DeclBase, DeclTableBase):
    __tablename__ = 'battery'
    id = Column(Integer, primary_key=True)

    plugged_in = Column(Boolean)
    temperature = Column(Integer)
    level = Column(Integer)
    ts = Column(Float)

    mapping = {
        'plugged_in': ('plugged', bool),
        'temperature': ('temperature', int),
        'level': ('level', int),
    }

engine = create_engine("sqlite:///{}".format(DB_PATH), echo=VERBOSE)

Base = automap_base(DeclBase)


class Data(Base):
    __tablename__ = "data"
    id = Column(String, primary_key=True)
    device = Column(String)
    probe = Column(String)
    timestamp = Column(Integer)
    value = Column(String)


def initialize():
    DeclBase.metadata.create_all(engine)
    Base.prepare(engine)

def get_session():
    return orm.sessionmaker(bind=engine)()

session = get_session()
