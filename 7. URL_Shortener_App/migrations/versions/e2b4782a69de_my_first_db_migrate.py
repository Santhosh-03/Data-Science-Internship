"""My first DB migrate

Revision ID: e2b4782a69de
Revises: 
Create Date: 2022-01-02 12:05:26.387568

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e2b4782a69de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('short_urls',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('long_url', sa.Text(), nullable=True),
    sa.Column('short_code', sa.Text(), nullable=True),
    sa.Column('short_url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('short_urls')
    # ### end Alembic commands ###
