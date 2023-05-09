"""empty message

Revision ID: 83ad80e75ce6
Revises: 
Create Date: 2023-05-09 11:46:04.265154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83ad80e75ce6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=80), nullable=False),
    sa.Column('city_ascii', sa.String(length=80), nullable=False),
    sa.Column('lat', sa.String(length=80), nullable=False),
    sa.Column('lng', sa.String(length=80), nullable=False),
    sa.Column('country', sa.String(length=80), nullable=False),
    sa.Column('iso2', sa.String(length=2), nullable=False),
    sa.Column('iso3', sa.String(length=3), nullable=False),
    sa.Column('admin_name', sa.String(length=80), nullable=False),
    sa.Column('capital', sa.String(length=80), nullable=True),
    sa.Column('population', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    op.drop_table('Data')
    # ### end Alembic commands ###