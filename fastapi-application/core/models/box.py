from sqlalchemy.orm import Mapped, mapped_column

from core.models import Base
from core.models.mixins.int_id_pk import IntIdPkMixin


class Box(IntIdPkMixin, Base):
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    price: Mapped[int]
