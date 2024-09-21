"""empty message

Revision ID: 1f5f9aaec2e6
Revises: 7ee94ad9658e
Create Date: 2024-09-21 10:45:08.257317

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f5f9aaec2e6'
down_revision = '7ee94ad9658e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users_auth',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.Column('update_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('users_auth', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_users_auth_email'), ['email'], unique=False)
        batch_op.create_index(batch_op.f('ix_users_auth_username'), ['username'], unique=False)

    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_column('password_hash')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password_hash', sa.VARCHAR(), nullable=True))

    with op.batch_alter_table('users_auth', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_users_auth_username'))
        batch_op.drop_index(batch_op.f('ix_users_auth_email'))

    op.drop_table('users_auth')
    # ### end Alembic commands ###
