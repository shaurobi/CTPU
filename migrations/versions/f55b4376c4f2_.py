"""empty message

Revision ID: f55b4376c4f2
Revises: a805aa0c410b
Create Date: 2017-08-02 15:31:45.710876

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f55b4376c4f2'
down_revision = 'a805aa0c410b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('enrolments', sa.Column('attended', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('enrolments', 'attended')
    # ### end Alembic commands ###
