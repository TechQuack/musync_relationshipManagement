"""empty message

Revision ID: 7ab358172c5d
Revises: e936de98007d
Create Date: 2024-04-06 07:52:25.620825

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7ab358172c5d'
down_revision = 'e936de98007d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_music_statistic',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('top_listened_artist', sa.String(), nullable=True),
    sa.Column('top_listened_music', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['top_listened_artist'], ['top_listened_artist.top_listened_artist'], ),
    sa.ForeignKeyConstraint(['top_listened_music'], ['top_listened_music.top_listened_music'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_music_statistic')
    # ### end Alembic commands ###
