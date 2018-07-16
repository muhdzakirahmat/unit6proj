"""Use strings for challenge types

Revision ID: 7e9efd084c5a
Revises: cbf5620f8e15
Create Date: 2017-10-04 16:40:16.508879

"""
from Unit6.models import db, Challenges
from alembic import op
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import text, table, column

# revision identifiers, used by Alembic.
revision = '7e9efd084c5a'
down_revision = 'cbf5620f8e15'
branch_labels = None
depends_on = None

challenges_table = table('challenges',
    column('type', db.Integer),
)


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    url = str(bind.engine.url)
    if url.startswith('mysql'):
        op.alter_column('challenges', 'type',
                   existing_type=sa.INTEGER(),
                   type_=sa.String(length=80),
                   existing_nullable=True)

        op.execute("UPDATE challenges set type='standard' WHERE type=0")
    elif url.startswith('postgres'):
        op.alter_column('challenges', 'type',
                   existing_type=sa.INTEGER(),
                   type_=sa.String(length=80),
                   existing_nullable=True,
                   postgresql_using="COALESCE(NULLIF(type, 0)::CHARACTER, 'standard')"
                   )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    bind = op.get_bind()
    url = str(bind.engine.url)
    if url.startswith('mysql'):
            op.execute("UPDATE challenges set type=0 WHERE type='standard'")

            op.alter_column('challenges', 'type',
                        existing_type=sa.String(length=80),
                        type_=sa.INTEGER(),
                        existing_nullable=True)
    elif url.startswith('postgres'):
        op.alter_column('challenges', 'type',
                    existing_type=sa.String(length=80),
                    type_=sa.INTEGER(),
                    existing_nullable=True,
                    postgresql_using="COALESCE(NULLIF(type, 'standard')::NUMERIC, 0)"
                    )
    # ### end Alembic commands ###
