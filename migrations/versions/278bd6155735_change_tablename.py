"""change tablename

Revision ID: 278bd6155735
Revises: 
Create Date: 2020-03-02 09:36:42.536816

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '278bd6155735'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('songs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_name', sa.String(), nullable=True),
    sa.Column('track_id', sa.String(), nullable=True),
    sa.Column('track_name', sa.String(), nullable=True),
    sa.Column('acousticness', sa.Float(), nullable=True),
    sa.Column('danceability', sa.Float(), nullable=True),
    sa.Column('duration_ms', sa.Integer(), nullable=True),
    sa.Column('energy', sa.Float(), nullable=True),
    sa.Column('instrumentalness', sa.Float(), nullable=True),
    sa.Column('key', sa.Integer(), nullable=True),
    sa.Column('liveness', sa.Float(), nullable=True),
    sa.Column('loudness', sa.Float(), nullable=True),
    sa.Column('mode', sa.Integer(), nullable=True),
    sa.Column('speechiness', sa.Float(), nullable=True),
    sa.Column('tempo', sa.Float(), nullable=True),
    sa.Column('time_signature', sa.Integer(), nullable=True),
    sa.Column('valence', sa.Float(), nullable=True),
    sa.Column('popularity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('song')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('song',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('artist_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('track_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('track_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('acousticness', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('danceability', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('duration_ms', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('energy', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('instrumentalness', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('key', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('liveness', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('loudness', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('mode', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('speechiness', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('tempo', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('time_signature', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('valence', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('popularity', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='song_pkey')
    )
    op.drop_table('songs')
    # ### end Alembic commands ###
