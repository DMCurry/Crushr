"""change schedule enum

Revision ID: 62aad929d98a
Revises: 31af7810c821
Create Date: 2025-02-26 15:48:24.084054

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.mysql import ENUM


# revision identifiers, used by Alembic.
revision: str = '62aad929d98a'
down_revision: Union[str, None] = '31af7810c821'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


# New Enum definition
new_enum = ENUM('MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN', name='dayenum')

# Old Enum definition (use your previous values)
old_enum = ENUM('MON', 'TUE', 'WED', 'THU', 'FRI', name='dayenum')

def upgrade() -> None:
    op.alter_column('weekly_schedule', 'day',
                    existing_type=old_enum,
                    type_=new_enum,
                    existing_nullable=False)

def downgrade() -> None:
    op.alter_column('weekly_schedule', 'day',
                    existing_type=new_enum,
                    type_=old_enum,
                    existing_nullable=False)
