from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Box
from schemas.box import BoxCreate


async def get_all_boxes(
    session: AsyncSession
) -> Sequence[Box]:
    stmt = select(Box).order_by(Box.id)
    result = await session.scalars(stmt)
    return result.all()

async def create_box(
    session: AsyncSession,
    box_create: BoxCreate,
) -> Box:
    box = Box(**box_create.model_dump())
    session.add(box)
    await session.commit()
    await session.refresh(box)
    return box