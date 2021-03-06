"""empty message

Revision ID: d483c0326947
Revises: 
Create Date: 2022-04-14 13:05:23.822388

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd483c0326947'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('plan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('plan_type', sa.Enum('basic', 'premium', name='provider_plan'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('client_provider',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('provider_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('plan_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], ),
    sa.ForeignKeyConstraint(['plan_id'], ['plan.id'], ),
    sa.ForeignKeyConstraint(['provider_id'], ['provider.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('journal_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('entry', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('date_entered', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['client.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('journal_entry')
    op.drop_table('client_provider')
    op.drop_table('provider')
    op.drop_table('plan')
    op.drop_table('client')
    # ### end Alembic commands ###
