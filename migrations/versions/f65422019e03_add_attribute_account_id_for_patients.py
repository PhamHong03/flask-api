"""add attribute account_id for patients

Revision ID: f65422019e03
Revises: ebd53bb9caef
Create Date: 2025-03-20 11:45:56.782004

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f65422019e03'
down_revision = 'ebd53bb9caef'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.add_column(sa.Column('account_id', sa.Integer(), nullable=False))
        batch_op.create_unique_constraint(None, ['account_id'])
        batch_op.create_foreign_key(None, 'accounts', ['account_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('patients', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('account_id')

    # ### end Alembic commands ###
