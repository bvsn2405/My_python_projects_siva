from sqlalchemy import Column, String, Integer

from database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(150))
    email = Column(String(150))
    password = Column(String(150))

    def __repr__(self):
        return '<User %r>' % self.id
