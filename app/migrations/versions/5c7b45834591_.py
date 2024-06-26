"""empty message

Revision ID: 5c7b45834591
Revises: 7e68aa7584c4
Create Date: 2024-05-15 16:23:13.565391

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5c7b45834591'
down_revision = '7e68aa7584c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.alter_column('match_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user1_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('user2_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('match', schema=None) as batch_op:
        batch_op.alter_column('user2_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('user1_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('match_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
