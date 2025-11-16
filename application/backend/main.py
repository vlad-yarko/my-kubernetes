from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .engine import get_session
from .models import Request


origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173"
]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],  
)


@app.get("/requests")
async def get_requests(session: AsyncSession = Depends(get_session())):
    stmt = (
        select(Request)
        .where(Request.id == True)
        .with_for_update()
    )
    result = await session.execute(stmt)
    requests_data = result.scalar_one()
    requests_data.count += 1
    await session.commit()
    await session.refresh(requests_data)
    return {
        "count": requests_data.count
    }
