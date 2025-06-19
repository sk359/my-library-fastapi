from sqlalchemy import create_engine

#The engine object acts as a central source of connections to a particular database, providing both a factory as
# well as a holding space called a connection pool for these database connections:
engine = create_engine("postgresql+psycopg://postgres:postgres@localhost/my_library", echo=True)