"""empty message

Revision ID: 7e68aa7584c4
Revises: 8e68bcc9fbce
Create Date: 2024-05-14 18:47:15.275701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7e68aa7584c4'
down_revision = '8e68bcc9fbce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('top_listened_artist', schema=None) as batch_op:
        batch_op.alter_column('top_listened_artist',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.drop_column('artist_id')

    with op.batch_alter_table('top_listened_music', schema=None) as batch_op:
        batch_op.alter_column('top_listened_music',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.alter_column('artist_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
        batch_op.drop_column('music_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('top_listened_music', schema=None) as batch_op:
        batch_op.add_column(sa.Column('music_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.alter_column('artist_name',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('top_listened_music',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    with op.batch_alter_table('top_listened_artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.alter_column('top_listened_artist',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)

    # ### end Alembic commands ###