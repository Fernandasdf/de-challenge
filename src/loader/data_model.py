from sqlalchemy import Column, ForeignKey, String, Float, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Company(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_name = Column(String, unique=True)

class Console(Base):
    __tablename__ = 'console'
    id = Column(Integer, primary_key=True, autoincrement=True)
    console_name = Column(String, unique=True)
    # console_company = relationship(ConsoleCompany, uselist=False, back_populates="console")


class Game(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True, autoincrement=True)
    game_name = Column(String, unique=True)


class ConsoleCompany(Base):
    __tablename__ = 'console_company'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey('company.id'))
    console_id = Column(Integer, ForeignKey('console.id'))
    console = relationship(Console)

class GameScore(Base):
    __tablename__ = 'game_score'
    console_id = Column(Integer, ForeignKey('console.id'), primary_key=True)
    game_id = Column(Integer, ForeignKey('game.id'), primary_key=True)
    release_dt = Column(Date)
    metascore = Column(Integer)
    userscore = Column(Integer)
    avg_score = Column(Float)
    game = relationship(Game)
    console = relationship(Console)