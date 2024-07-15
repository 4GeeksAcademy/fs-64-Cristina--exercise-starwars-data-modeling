import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)

    def to_dict(self):
        return {}

class UniverseAsset(Base):
    __tablename__ = 'universeasset'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=False)


class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    universeasset_id = Column(Integer, ForeignKey('universeasset.id'))
    universeasset= relationship(UniverseAsset)

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    universeasset_id = Column(Integer, ForeignKey('universeasset.id'))
    universeasset= relationship(UniverseAsset)

class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)
    universeasset_id = Column(Integer, ForeignKey('universeasset.id'))
    universeasset= relationship(UniverseAsset)
    


class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    universeasset_id = Column(Integer, ForeignKey('universeasset.id'))
    universeasset= relationship(UniverseAsset)
    favorite_id = Column(String(250), nullable=False)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
