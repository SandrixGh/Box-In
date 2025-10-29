from sqlalchemy.ext.asyncio import AsyncSession

from models import db_helper


def create_db_context() -> AsyncSession:
    return db_helper.session_getter()