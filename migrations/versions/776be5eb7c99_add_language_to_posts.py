"""add language to posts

Revision ID: 776be5eb7c99
Revises: 64ee45356184
Create Date: 2022-04-11 10:37:09.795019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '776be5eb7c99'
down_revision = '64ee45356184'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.String(length=5), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###
