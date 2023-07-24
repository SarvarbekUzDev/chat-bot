from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


# User table
class Users(Base):
    __tablename__ = "users"
    
    id = Column("id",Integer,primary_key=True,autoincrement=True) # ssn bu id
    chat_id = Column("chat_id",Integer,unique=True)
    fullname = Column("fullname",String(200))
    is_admin = Column("is_admin", Boolean, default=False)


    def __init__(self, chat_id, fullname, is_admin=False):
        # self.id = id
        self.fullname = fullname
        self.chat_id  = chat_id
        self.is_admin = is_admin
    
    def __repr__(self) -> str:
        return f"{self.id} - {self.fullname} - {self.chat_id}"
    
    # def test(self):
    #     print("--------OK---Tested-----")
    