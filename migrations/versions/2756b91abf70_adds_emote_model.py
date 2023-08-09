"""adds emote model

Revision ID: 2756b91abf70
Revises: 
Create Date: 2023-06-28 15:38:29.460757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2756b91abf70'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('emote',
    sa.Column('emote_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('emote_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('emote')
    # ### end Alembic commands ###