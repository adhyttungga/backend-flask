"""create posts table

Revision ID: bd13748b3f2d
Revises: bfea073458de
Create Date: 2021-07-08 16:23:26.441308

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd13748b3f2d'
down_revision = 'bfea073458de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('content', sa.Text(), nullable=True),
    sa.Column('category', sa.String(length=100), nullable=True),
    sa.Column('created_date', sa.DateTime(), nullable=True),
    sa.Column('updated_date', sa.DateTime(), nullable=True),
    sa.Column('status', sa.Enum('Publish', 'Draft', 'Thrash', name='postsStatus'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('posts')
    # ### end Alembic commands ###
