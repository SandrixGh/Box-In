from sqlalchemy.orm import Mapped, mapped_column

from models import Base
from models.mixins.int_id_pk import IntIdPkMixin


class Box(IntIdPkMixin, Base):
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[str]
    price: Mapped[int]
