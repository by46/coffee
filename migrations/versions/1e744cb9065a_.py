"""empty message

Revision ID: 1e744cb9065a
Revises: 7eb9068ca028
Create Date: 2016-11-22 10:47:18.224000

"""

# revision identifiers, used by Alembic.
revision = '1e744cb9065a'
down_revision = '7eb9068ca028'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'coffee', 'vendor', ['vendor_id'], ['id'])
    op.create_foreign_key(None, 'coffee_vendor', 'coffee', ['coffee_id'], ['id'])
    op.create_foreign_key(None, 'coffee_vendor', 'vendor', ['vendor_id'], ['id'])
    op.add_column('demo3', sa.Column('name', sa.String(length=30), nullable=True))
    op.create_index('idx_demo3_name', 'demo3', ['name'], unique=False)
    op.create_foreign_key(None, 'feedback', 'coffee', ['coffee_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'feedback', type_='foreignkey')
    op.drop_index('idx_demo3_name', table_name='demo3')
    op.drop_column('demo3', 'name')
    op.drop_constraint(None, 'coffee_vendor', type_='foreignkey')
    op.drop_constraint(None, 'coffee_vendor', type_='foreignkey')
    op.drop_constraint(None, 'coffee', type_='foreignkey')
    ### end Alembic commands ###