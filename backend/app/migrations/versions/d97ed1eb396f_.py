"""empty message

Revision ID: d97ed1eb396f
Revises: f64620410f92
Create Date: 2024-11-11 17:53:57.152459

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd97ed1eb396f'
down_revision = 'f64620410f92'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Address', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('City', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('State', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('PhoneNumber', sa.String(length=255), nullable=False))
        batch_op.add_column(sa.Column('IsAdmin', sa.String(length=255), nullable=False))
        batch_op.alter_column('Email',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.alter_column('Email',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.drop_column('IsAdmin')
        batch_op.drop_column('PhoneNumber')
        batch_op.drop_column('State')
        batch_op.drop_column('City')
        batch_op.drop_column('Address')

    # ### end Alembic commands ###