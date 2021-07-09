"""create posts table

Revision ID: d3c69092f92a
Revises: 7971be78752e
Create Date: 2021-07-08 15:05:55.708301

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd3c69092f92a'
down_revision = '7971be78752e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'status',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('posts', 'status',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)
    # ### end Alembic commands ###