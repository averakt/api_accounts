"""initial resource

Revision ID: 3f9e6ffcd7a5
Revises: 0343a057d57c
Create Date: 2023-10-21 23:52:59.010078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f9e6ffcd7a5'
down_revision = '0343a057d57c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funds',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brief', sa.String(length=3), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('code', sa.String(length=3), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_funds_brief'), 'funds', ['brief'], unique=True)
    op.create_index(op.f('ix_funds_code'), 'funds', ['code'], unique=True)
    op.create_table('resource',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('brief', sa.String(length=20), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('fund_id', sa.Integer(), nullable=True),
    sa.Column('dateStart', sa.DateTime(), nullable=True),
    sa.Column('dateEnd', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fund_id'], ['funds.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('resource')
    op.drop_index(op.f('ix_funds_code'), table_name='funds')
    op.drop_index(op.f('ix_funds_brief'), table_name='funds')
    op.drop_table('funds')
    # ### end Alembic commands ###