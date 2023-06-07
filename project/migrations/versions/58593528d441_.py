"""empty message

Revision ID: 58593528d441
Revises: 959b2141a2f8
Create Date: 2023-05-31 17:08:38.654364

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '58593528d441'
down_revision = '959b2141a2f8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('payroll',
    sa.Column('payroll_id', sa.Integer(), nullable=False),
    sa.Column('payrate', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('gross_pay', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('tax', sa.Numeric(precision=5, scale=2), nullable=True),
    sa.Column('net_pay', sa.Numeric(precision=8, scale=2), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('attendance_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['attendance_id'], ['attendance.attendance_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], ),
    sa.PrimaryKeyConstraint('payroll_id')
    )
    op.drop_table('pay_roll')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pay_roll',
    sa.Column('payroll_id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('payrate', mysql.DECIMAL(precision=8, scale=2), nullable=True),
    sa.Column('gross_pay', mysql.DECIMAL(precision=8, scale=2), nullable=True),
    sa.Column('tax', mysql.DECIMAL(precision=5, scale=2), nullable=True),
    sa.Column('net_pay', mysql.DECIMAL(precision=8, scale=2), nullable=True),
    sa.Column('user_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('attendance_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['attendance_id'], ['attendance.attendance_id'], name='pay_roll_ibfk_2'),
    sa.ForeignKeyConstraint(['user_id'], ['user.user_id'], name='pay_roll_ibfk_1'),
    sa.PrimaryKeyConstraint('payroll_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('payroll')
    # ### end Alembic commands ###