"""adding vibe_score column

Revision ID: bd015e097fb6
Revises: 9169f1c37279
Create Date: 2023-05-22 00:44:05.877663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bd015e097fb6'
down_revision = '9169f1c37279'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_playlist')
    op.add_column('playlists', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'playlists', 'users', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'playlists', type_='foreignkey')
    op.drop_column('playlists', 'user_id')
    op.create_table('user_playlist',
    sa.Column('user_playlist_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('playlist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['playlist_id'], ['playlists.playlist_id'], name='user_playlist_playlist_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='user_playlist_user_id_fkey'),
    sa.PrimaryKeyConstraint('user_playlist_id', name='user_playlist_pkey')
    )
    # ### end Alembic commands ###
