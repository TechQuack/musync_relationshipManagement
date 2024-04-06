"""empty message

Revision ID: e936de98007d
Revises: f0595006b4fd
Create Date: 2024-04-06 07:38:03.615346

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e936de98007d'
down_revision = 'f0595006b4fd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('top_listened_artist',
    sa.Column('top_listened_artist', sa.String(length=255), nullable=False),
    sa.Column('top_ranking', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('top_listened_artist')
    )
    op.create_table('top_listened_music',
    sa.Column('top_listened_music', sa.String(length=255), nullable=False),
    sa.Column('artist_name', sa.String(length=255), nullable=True),
    sa.Column('top_ranking', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('top_listened_music')
    )
    op.create_table('user',
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
    op.drop_table('cat')
    op.drop_table('entity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('entity',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('lastname', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('bio', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('osecour', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='entity_pkey'),
    sa.UniqueConstraint('email', name='entity_email_key')
    )
    op.create_table('cat',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('firstname', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('lastname', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=80), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('osecour', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('bio', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='cat_pkey'),
    sa.UniqueConstraint('email', name='cat_email_key')
    )
    op.drop_table('user')
    op.drop_table('top_listened_music')
    op.drop_table('top_listened_artist')
    # ### end Alembic commands ###