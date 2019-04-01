from orm import model
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.orm import sessionmaker
session = sessionmaker()()


# 注册的时候调用它
def insertUser(username, password):
    result = session.add(model.User(username=username, password=password))
    session.commit()
    session.close()


def checkUser(username,password):
    result = session.query(model.User).filter(model.User.username==username).filter(model.User.password==password).first().id
    if result:
        return result
    else:
        return -1

