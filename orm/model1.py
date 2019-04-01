class Goods():
    def __init__(self, id, name, price, number):
        self.id = id
        self.name = name
        self.price = price
        self.number = number

    def __str__(self):
        return "id:%s name:%s price:%s number:%s"%(self.id, self.name, self.price, self.number)


from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:123456@localhost/flaskdb",
                                    encoding='utf8', echo=True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(bind=engine)

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'food'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False )
    username = Column(String(20), nullable=False)
    password = Column(String(50), nullable=False)


if __name__ == "__main__":
    # 创建表   必须写在main模块
    # print(engine)
    Base.metadata.create_all(bind=engine)
