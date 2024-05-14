"""empty message

Revision ID: 1b7121f16981
Revises: 
Create Date: 2024-04-06 09:22:53.521102

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b7121f16981'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feedback',
    sa.Column('match_id', sa.Integer(), nullable=False),
    sa.Column('score_user1', sa.Integer(), nullable=True),
    sa.Column('score_user2', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('match_id')
    )
    op.create_table('musync_user',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('is_certified', sa.Boolean(), nullable=False),
    sa.Column('birthdate', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('gender', sa.String(length=50), nullable=False),
    sa.Column('accepted_age_gap', sa.Integer(), nullable=True),
    sa.Column('accepted_distance', sa.Integer(), nullable=True),
    sa.Column('targeted_gender', sa.String(length=50), nullable=True),
    sa.Column('favorite_musician', sa.Integer(), nullable=True),
    sa.Column('favorite_music', sa.Integer(), nullable=True),
    sa.Column('favorite_musical_style', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('gender')
    )
    op.create_table('top_listened_artist',
    sa.Column('top_listened_artist', sa.String(length=255), nullable=False),
    sa.Column('top_ranking', sa.Integer(), nullable=False),
    )
    op.create_table('top_listened_music',
    sa.Column('top_listened_music', sa.String(length=255), nullable=False),
    sa.Column('artist_name', sa.String(length=255), nullable=True),
    sa.Column('top_ranking', sa.Integer(), nullable=False),
    )
    op.create_table('match',
    sa.Column('match_id', sa.Integer(), nullable=False),
    sa.Column('user1_id', sa.Integer(), nullable=True),
    sa.Column('user2_id', sa.Integer(), nullable=True),
    sa.Column('match_compatibility', sa.Integer(), nullable=True),
    sa.Column('status_code', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user1_id'], ['musync_user.user_id'], ),
    sa.ForeignKeyConstraint(['user2_id'], ['musync_user.user_id'], ),
    sa.PrimaryKeyConstraint('match_id')
    )
    op.create_table('user_music_statistic',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('top_listened_artist', sa.String(), nullable=True),
    sa.Column('top_listened_music', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['musync_user.user_id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_music_statistic')
    op.drop_table('match')
    op.drop_table('top_listened_music')
    op.drop_table('top_listened_artist')
    op.drop_table('musync_user')
    op.drop_table('feedback')
    # ### end Alembic commands ###
