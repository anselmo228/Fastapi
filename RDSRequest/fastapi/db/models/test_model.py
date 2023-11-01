from sqlalchemy import Column, String, Integer, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from db.session import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)


class Users(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String)
    created_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP, default=None)



