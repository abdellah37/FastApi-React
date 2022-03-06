"""create_main_tables

Revision ID: 33f4779fb739
Revises: 
Create Date: 2021-12-27 15:02:07.134119

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic
revision = '33f4779fb739'
down_revision = None
branch_labels = None
depends_on = None


def create_cleanings_table() -> None:
    op.create_table(
        "cleanings",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.Text, nullable=False, index=True),
        sa.Column("description", sa.Text, nullable=True),
        sa.Column("cleaning_type", sa.Text, nullable=False, server_default="spot_clean"),
        sa.Column("price", sa.Numeric(10, 2), nullable=False),
    )

def upgrade() -> None:
    create_cleanings_table()
    pass


def downgrade() -> None:
    op.drop_table("cleanings")
    pass

