from typing import Annotated

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import db_helper
from crud import boxes as boxes_crud
from schemas.box import BoxRead, BoxCreate

router = APIRouter(
    tags=["Boxes"],
)

@router.get("", response_model=list[BoxRead])
async def get_boxes(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)
    ],
):
    boxes = await boxes_crud.get_all_boxes(session=session)
    return boxes

@router.post("", response_model=BoxRead)
async def create_box(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)
    ],
    box_create: BoxCreate
):
    box = await boxes_crud.create_box(session=session, box_create=box_create)
    return box