"""create orders table

Revision ID: 0f2f73d40d4d
Revises: abce90031b82
Create Date: 2025-07-13 13:14:18.820741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f2f73d40d4d'
down_revision: Union[str, Sequence[str], None] = 'abce90031b82'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
