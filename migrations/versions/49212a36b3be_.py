"""empty message

Revision ID: 49212a36b3be
Revises: 23c3a8c2cc2b
Create Date: 2022-10-05 20:48:47.682658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49212a36b3be'
down_revision = '23c3a8c2cc2b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_active', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_active')
    # ### end Alembic commands ###
