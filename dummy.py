import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tabledef import *

engine = create_engine('sqlite:///tutorial.db', echo=True)


Session = sessionmaker(bind=engine)
session = Session()

user = User("123","123")
session.add(user)

user = User("python123","python")
session.add(user)

user = User("chico","python")
session.add(user)


session.commit()

session.commit()
