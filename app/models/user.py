from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from app.db.session import Base


class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key=True, index=True)
	username = Column(String(50), unique=True, index=True, nullable=False)
	hashed_password = Column(String(255), nullable=False)
	created_at = Column(DateTime(timezone=True), server_default=func.now())

	sent_messages = relationship("Message", back_populates="sender", foreign_keys="Message.sender_id")
	received_messages = relationship("Message", back_populates="receiver", foreign_keys="Message.receiver_id")
