"""Comments model

Revision ID: 90c297c08ae5
Revises: 6845a87e71a9
Create Date: 2022-08-11 18:29:15.272149

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '90c297c08ae5'
down_revision = '6845a87e71a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.Text(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('news_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['news_id'], ['news.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comments_news_id'), 'comments', ['news_id'], unique=False)
    op.create_index(op.f('ix_comments_user_id'), 'comments', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comments_user_id'), table_name='comments')
    op.drop_index(op.f('ix_comments_news_id'), table_name='comments')
    op.drop_table('comments')
    # ### end Alembic commands ###
