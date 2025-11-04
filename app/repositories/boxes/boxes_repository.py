from typing import Sequence

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models import Box
from repositories.dependencies.db_context import create_db_context
from schemas.boxes.box import BoxRead, BoxCreate, BoxUpdate


async def get_all_boxes(
    context: AsyncSession = Depends(create_db_context),
) -> Sequence[Box]:
    stmt = select(Box).order_by(Box.id)
    result = await context.scalars(stmt)
    return result.all()


async def get_box_by_id(
    box_id: int,
    context: AsyncSession = Depends(create_db_context),
) -> BoxRead:
    stmt = select(Box).where(Box.id == box_id)
    result = await context.scalar(stmt)
    return BoxRead.model_validate(result)


async def create_box(
    box_data: BoxCreate,
    context: AsyncSession = Depends(create_db_context),
) -> BoxRead:
    box = Box(**box_data.model_dump())
    context.add(box)
    await context.commit()
    await context.refresh(box)
    return BoxRead.model_validate(box)


async def update_box(
    box_id: int,
    update_data: BoxUpdate,
    context: AsyncSession = Depends(create_db_context)
) -> BoxRead:
    stmt = select(Box).where(Box.id == box_id)
    box = await context.scalar(stmt)

    update_dict = update_data.model_dump(exclude_unset=True)
    for field, value in update_dict.items():
        setattr(box, field, value)

    await context.commit()
    await context.refresh(box)

    return BoxRead.model_validate(box)


async def delete_box(
    box_id: int,
    context: AsyncSession = Depends(create_db_context)
) -> None:

    stmt = select(Box).where(Box.id == box_id)
    box = await context.scalar(stmt)

    await context.delete(box)
    await context.commit()

    return None






























