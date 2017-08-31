"""empty message

Revision ID: d4871fcdd805
Revises: 71d0f6372175
Create Date: 2017-08-15 09:26:23.444097

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4871fcdd805'
down_revision = '71d0f6372175'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('responseerror', sa.Column('json', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('responseerror', 'json')
    # ### end Alembic commands ###