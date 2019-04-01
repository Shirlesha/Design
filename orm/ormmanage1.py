from orm import model1
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.orm import sessionmaker
session = sessionmaker()()


# 注册的时候调用它
def insertUser(username, password):
    result = session.add(model1.User(username=username, password=password))
    session.commit()
    session.close()


def checkUser(username, password):
    result = session.query(model1.User).filter(model1.User.username==username).filter(model1.User.password==password).first().id
    if result:
        return result
    else:
        return -1

