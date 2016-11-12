"""empty message

Revision ID: 36acc74fe688
Revises: af09e1841336
Create Date: 2016-11-12 16:13:23.089000

"""

# revision identifiers, used by Alembic.
revision = '36acc74fe688'
down_revision = 'af09e1841336'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('coffee', sa.Column('imported', sa.Boolean(), nullable=True))
    op.create_foreign_key(None, 'coffee', 'vendor', ['vendor_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'coffee', type_='foreignkey')
    op.drop_column('coffee', 'imported')
    ### end Alembic commands ###
