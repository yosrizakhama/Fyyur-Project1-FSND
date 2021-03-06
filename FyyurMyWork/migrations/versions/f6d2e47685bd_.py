"""empty message

Revision ID: f6d2e47685bd
Revises: 5af0eade0b7a
Create Date: 2020-09-16 11:19:27.188247

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6d2e47685bd'
down_revision = '5af0eade0b7a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('Artist', 'city_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('City', sa.Column('city', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('City', 'city')
    op.alter_column('Artist', 'city_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
