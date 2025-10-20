from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, declared_attr
from sqlalchemy.orm import mapped_column

class IntIdPkMixin:
    @declared_attr
    def box_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("boxes.id", ondelete="SET NULL"),
            unique=True,
            nullable=True,
        )