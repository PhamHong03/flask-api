"""change type of attributes

Revision ID: 4cd5851f837d
Revises: b76100ee6135
Create Date: 2025-03-19 12:37:27.041737

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '4cd5851f837d'
down_revision = 'b76100ee6135'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('day_of_birth', sa.BigInteger(), nullable=False))
        batch_op.alter_column('status',
               existing_type=mysql.INTEGER(display_width=11),
               type_=sa.String(length=100),
               existing_nullable=False)
        batch_op.drop_column('dateofbirth')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('dateofbirth', mysql.BIGINT(display_width=20), autoincrement=False, nullable=False))
        batch_op.alter_column('status',
               existing_type=sa.String(length=100),
               type_=mysql.INTEGER(display_width=11),
               existing_nullable=False)
        batch_op.drop_column('day_of_birth')

    # ### end Alembic commands ###
