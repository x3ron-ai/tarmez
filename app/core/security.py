from datetime import datetime, timedelta, timezone
from typing import Optional, Any, Dict
from jose import jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
	return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
	return pwd_context.hash(password)

def create_access_token(data: Dict[str, Any], expires_minutes: Optional[int] = None) -> str:
	to_encode = data.copy()
	exp_minutes = expires_minutes or settings.access_token_expire_minutes
	expire = datetime.now(timezone.utc) + timedelta(minutes=exp_minutes)
	to_encode.update({"exp": expire})
	return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

