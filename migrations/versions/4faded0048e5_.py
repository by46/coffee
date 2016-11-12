"""empty message

Revision ID: 4faded0048e5
Revises: 36acc74fe688
Create Date: 2016-11-12 17:01:45.875000

"""

# revision identifiers, used by Alembic.
revision = '4faded0048e5'
down_revision = '36acc74fe688'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'coffee', 'vendor', ['vendor_id'], ['id'])
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'coffee', type_='foreignkey')
    ### end Alembic commands ###
