"""book_keyword_col

Revision ID: 9272a83eb64e
Revises: daa49ade0391
Create Date: 2025-06-19 17:31:10.139498

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '9272a83eb64e'
down_revision: Union[str, Sequence[str], None] = 'daa49ade0391'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('books', sa.Column('keywords', postgresql.ARRAY(sa.String()), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('books', 'keywords')
    # ### end Alembic commands ###
