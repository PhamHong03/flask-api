"""change type Date to attributes

Revision ID: ebd53bb9caef
Revises: 4cd5851f837d
Create Date: 2025-03-19 14:09:53.226999

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ebd53bb9caef'
down_revision = '4cd5851f837d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('day_of_birth',
               existing_type=mysql.BIGINT(display_width=20),
               type_=sa.Date(),
               existing_nullable=False)
        batch_op.alter_column('code_card_day_start',
               existing_type=mysql.BIGINT(display_width=20),
               type_=sa.Date(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.alter_column('code_card_day_start',
               existing_type=sa.Date(),
               type_=mysql.BIGINT(display_width=20),
               existing_nullable=False)
        batch_op.alter_column('day_of_birth',
               existing_type=sa.Date(),
               type_=mysql.BIGINT(display_width=20),
               existing_nullable=False)

    # ### end Alembic commands ###
