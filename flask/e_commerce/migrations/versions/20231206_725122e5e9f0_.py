"""empty message

Revision ID: 725122e5e9f0
Revises: 806406f4079f
Create Date: 2023-12-06 15:18:43.086425

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '725122e5e9f0'
down_revision = '806406f4079f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('orders_product_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])
        batch_op.drop_column('product_id')

    with op.batch_alter_table('product_order', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.NUMERIC(),
               type_=sa.Float(),
               existing_nullable=False)

    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('vendor_id', sa.Integer(), nullable=False))
        batch_op.drop_constraint('products_category_key', type_='unique')
        batch_op.drop_constraint('products_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'vendors', ['vendor_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('products', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('products_user_id_fkey', 'vendors', ['user_id'], ['id'])
        batch_op.create_unique_constraint('products_category_key', ['category'])
        batch_op.drop_column('vendor_id')

    with op.batch_alter_table('product_order', schema=None) as batch_op:
        batch_op.alter_column('amount',
               existing_type=sa.Float(),
               type_=sa.NUMERIC(),
               existing_nullable=False)

    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('orders_product_id_fkey', 'products', ['product_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
