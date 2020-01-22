from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:@localhost:3306/belajar',implicit_returning=False)
Session = sessionmaker(bind=engine)
session = Session()