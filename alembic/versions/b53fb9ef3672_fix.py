"""fix

Revision ID: b53fb9ef3672
Revises: 
Create Date: 2023-05-22 23:22:39.931459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b53fb9ef3672'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vibe')
    op.drop_constraint('playlist_track_playlist_id_fkey', 'playlist_track', type_='foreignkey')
    op.create_foreign_key(None, 'playlist_track', 'playlists', ['playlist_id'], ['playlist_id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'playlist_track', type_='foreignkey')
    op.create_foreign_key('playlist_track_playlist_id_fkey', 'playlist_track', 'playlists', ['playlist_id'], ['playlist_id'])
    op.create_table('vibe',
    sa.Column('vibe_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('vibe', sa.TEXT(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('vibe_id', name='vibe_pkey')
    )
    # ### end Alembic commands ###