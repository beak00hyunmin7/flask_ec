"""empty message

Revision ID: 74dfadbd6a5a
Revises: 1f5f9aaec2e6
Create Date: 2024-11-02 10:23:46.407259

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74dfadbd6a5a'
down_revision = '1f5f9aaec2e6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###