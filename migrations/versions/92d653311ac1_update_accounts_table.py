"""Update accounts table

Revision ID: 92d653311ac1
Revises: 2901d723c817
Create Date: 2025-03-22 12:25:22.778558

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '92d653311ac1'
down_revision = '2901d723c817'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.drop_column('username')
        batch_op.drop_column('phone_number')

    with op.batch_alter_table('physicians', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['account_id'])
        batch_op.create_foreign_key(None, 'accounts', ['account_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('physicians', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')

    with op.batch_alter_table('accounts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('phone_number', mysql.VARCHAR(length=100), nullable=False))
        batch_op.add_column(sa.Column('username', mysql.VARCHAR(length=255), nullable=False))

    # ### end Alembic commands ###
