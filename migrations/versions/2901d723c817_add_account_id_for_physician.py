from alembic import op
import sqlalchemy as sa
import sqlalchemy.engine.reflection

# revision identifiers, used by Alembic
revision = '2901d723c817'
down_revision = 'ce3fadf5e9be'
branch_labels = None
depends_on = None

def upgrade():
    # Kết nối database để kiểm tra schema
    bind = op.get_bind()
    inspector = sqlalchemy.engine.reflection.Inspector.from_engine(bind)

    # Lấy danh sách cột hiện có trong bảng 'physicians'
    columns = [col['name'] for col in inspector.get_columns('physicians')]

    with op.batch_alter_table('physicians', schema=None) as batch_op:
        if 'account_id' not in columns:
            batch_op.add_column(sa.Column('account_id', sa.Integer(), nullable=False))
            batch_op.create_unique_constraint('uq_physicians_account_id', ['account_id'])
            batch_op.create_foreign_key('fk_physicians_account_id', 'accounts', ['account_id'], ['id'])

def downgrade():
    with op.batch_alter_table('physicians', schema=None) as batch_op:
        batch_op.drop_constraint('fk_physicians_account_id', type_='foreignkey')
        batch_op.drop_constraint('uq_physicians_account_id', type_='unique')
        batch_op.drop_column('account_id')
