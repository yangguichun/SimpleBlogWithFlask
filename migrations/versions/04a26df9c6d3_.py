"""empty message

Revision ID: 04a26df9c6d3
Revises: 4ed84444672c
Create Date: 2018-08-29 07:14:44.779039

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04a26df9c6d3'
down_revision = '4ed84444672c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_user_email', table_name='user')
    op.drop_column('user', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
    op.create_index('ix_user_email', 'user', ['email'], unique=True)
    # ### end Alembic commands ###
