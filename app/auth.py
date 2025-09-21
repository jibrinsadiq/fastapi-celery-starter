import os, jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer


auth = HTTPBearer()
ALGS = ["RS256", "HS256"]
PUBKEY = os.getenv("JWT_PUBLIC_KEY", "")
SECRET = os.getenv("JWT_SECRET", "")


def get_current_user(creds=Depends(auth)):
token = creds.credentials
try:
if PUBKEY:
return jwt.decode(token, PUBKEY, algorithms=["RS256"])
if SECRET:
return jwt.decode(token, SECRET, algorithms=["HS256"])
raise HTTPException(500, "JWT keys not configured")
except jwt.PyJWTError:
raise HTTPException(401, "Invalid token")
