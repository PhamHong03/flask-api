"""create model patient

Revision ID: 6b4c50f636fb
Revises: 45dace7c9c16
Create Date: 2025-03-13 08:47:38.223760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6b4c50f636fb'
down_revision = '45dace7c9c16'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('dateofbirth', sa.BigInteger(), nullable=False),
    sa.Column('gender', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('job', sa.String(length=255), nullable=False),
    sa.Column('medical_code_card', sa.String(length=255), nullable=False),
    sa.Column('code_card_day_start', sa.BigInteger(), nullable=False),
    sa.Column('status', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    # ### end Alembic commands ###
