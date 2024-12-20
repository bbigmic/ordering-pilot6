"""Initial database migration

Revision ID: b402b0504a9e
Revises: 
Create Date: 2024-12-17 19:17:37.882135

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b402b0504a9e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('menu_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contains_alcohol', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('available', sa.Boolean(), nullable=True))

    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tip', sa.Float(), nullable=True))
        batch_op.add_column(sa.Column('nip', sa.String(length=15), nullable=True))
        batch_op.add_column(sa.Column('estimated_completion_time', sa.DateTime(), nullable=True))

    with op.batch_alter_table('order_item', schema=None) as batch_op:
        batch_op.add_column(sa.Column('takeaway', sa.Boolean(), nullable=True))

    with op.batch_alter_table('table', schema=None) as batch_op:
        batch_op.drop_constraint('table_qr_secret_key', type_='unique')
        batch_op.drop_column('qr_secret')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('table', schema=None) as batch_op:
        batch_op.add_column(sa.Column('qr_secret', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
        batch_op.create_unique_constraint('table_qr_secret_key', ['qr_secret'])

    with op.batch_alter_table('order_item', schema=None) as batch_op:
        batch_op.drop_column('takeaway')

    with op.batch_alter_table('order', schema=None) as batch_op:
        batch_op.drop_column('estimated_completion_time')
        batch_op.drop_column('nip')
        batch_op.drop_column('tip')

    with op.batch_alter_table('menu_item', schema=None) as batch_op:
        batch_op.drop_column('available')
        batch_op.drop_column('contains_alcohol')

    # ### end Alembic commands ###
