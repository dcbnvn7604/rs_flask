"""empty message

Revision ID: a6719a702c79
Revises: 7ac7c45748f5
Create Date: 2020-12-01 09:43:49.747018

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6719a702c79'
down_revision = '7ac7c45748f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    permission = op.create_table('permission',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user_permission',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('permission_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['permission.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.UniqueConstraint('user_id', 'permission_id')
    )
    # ### end Alembic commands ###

    op.bulk_insert(permission, [
        {'name': 'entry.create'},
        {'name': 'entry.update'},
        {'name': 'entry.delete'},
    ])


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_permission')
    op.drop_table('permission')
    # ### end Alembic commands ###
