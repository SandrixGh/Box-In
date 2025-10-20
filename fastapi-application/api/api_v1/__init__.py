from fastapi import APIRouter

from core.config import settings

from .boxes import router as boxes_router

router = APIRouter(
    prefix=settings.api.v1.prefix,
)
router.include_router(
    boxes_router,
    prefix=settings.api.v1.boxes,
)