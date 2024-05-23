"""termo

Revision ID: 820c4371e974
Revises: c48007820e6b
Create Date: 2024-05-23 18:53:03.699304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '820c4371e974'
down_revision = 'c48007820e6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('palavra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('palavra', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('palavra')
    # ### end Alembic commands ###
