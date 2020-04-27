import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('postgres://ptlzyvkzslpgpv:9b5752ab21dbfe8a7f77e107aae67f61fa7dd582e8c24bae4994ad1d65448367@ec2-54-75-231-215.eu-west-1.compute.amazonaws.com:5432/d2hrvppc8dqgpm')
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("books.csv")
    reader = csv.reader(f)
    next(reader, None)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books (isbn, title, author, year) VALUES (:isbn, :title, :author, :year)",
            {"isbn": isbn, "title": title, "author": author, "year": year})
    db.commit()