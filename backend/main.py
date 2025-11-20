from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas.user import UserCreate, UserOut
from crud.user import create_user

app = FastAPI(title="Website Builder AI", version="0.1.0")

@app.post("/signup", response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def signup(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await create_user(db, user)
    if not db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    return db_user

@app.get("/")
async def root():
    return {"message": "Website Builder AI - Signup is ready!"}