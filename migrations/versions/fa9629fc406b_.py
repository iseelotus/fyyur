"""empty message

Revision ID: fa9629fc406b
Revises: 
Create Date: 2020-03-29 21:17:50.242996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa9629fc406b'
down_revision = None
branch_labels = None
depends_on = None

def seed_data():
    venues_table = sa.sql.table('venues', 
        sa.sql.column('id', sa.Integer),
        sa.sql.column('name', sa.String),
        sa.sql.column('genres', sa.ARRAY(sa.String)),
        sa.sql.column('address', sa.String),
        sa.sql.column('city', sa.String),
        sa.sql.column('state', sa.String),
        sa.sql.column('phone', sa.String),
        sa.sql.column('website', sa.String),
        sa.sql.column('facebook_link', sa.String),
        sa.sql.column('seeking_talent', sa.Boolean),
        sa.sql.column('seeking_description', sa.String),
        sa.sql.column('image_link', sa.String)
    )
    artists_table = sa.sql.table('artists',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('name', sa.String),
        sa.sql.column('genres', sa.ARRAY(sa.String)),
        sa.sql.column('city', sa.String),
        sa.sql.column('state', sa.String),
        sa.sql.column('phone', sa.String),
        sa.sql.column('facebook_link', sa.String),
        sa.sql.column('seeking_venue', sa.Boolean),
        sa.sql.column('seeking_description', sa.String),
        sa.sql.column('image_link', sa.String)
    )
    shows_table = sa.sql.table('shows',
        sa.sql.column('id', sa.Integer),
        sa.sql.column('venue_id', sa.Integer),
        sa.sql.column('artist_id', sa.Integer),
        sa.sql.column('start_time', sa.DateTime),
    )

    op.bulk_insert(
        venues_table,
        [{"id": 1,
        "name": "The Musical Hop",
        "genres": ["Jazz", "Reggae", "Swing", "Classical", "Folk"],
        "address": "1015 Folsom Street",
        "city": "San Francisco",
        "state": "CA",
        "phone": "123-123-1234",
        "website": "https://www.themusicalhop.com",
        "facebook_link": "https://www.facebook.com/TheMusicalHop",
        "seeking_talent": True,
        "seeking_description": "We are on the lookout for a local artist to play every two weeks. Please call us.",
        "image_link": "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"
        },
        {"id": 2,
        "name": "The Dueling Pianos Bar",
        "genres": ["Classical", "R&B", "Hip-Hop"],
        "address": "335 Delancey Street",
        "city": "New York",
        "state": "NY",
        "phone": "914-003-1132",
        "website": "https://www.theduelingpianos.com",
        "facebook_link": "https://www.facebook.com/theduelingpianos",
        "seeking_talent": False,
        "seeking_description": "",
        "image_link": "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"
        },
        { "id": 3,
        "name": "Park Square Live Music & Coffee",
        "genres": ["Rock n Roll", "Jazz", "Classical", "Folk"],
        "address": "34 Whiskey Moore Ave",
        "city": "San Francisco",
        "state": "CA",
        "phone": "415-000-1234",
        "website": "https://www.parksquarelivemusicandcoffee.com",
        "facebook_link": "https://www.facebook.com/ParkSquareLiveMusicAndCoffee",
        "seeking_talent": False,
        "seeking_description": "",
        "image_link": "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"
        }]
    )

    op.bulk_insert(
        artists_table,
        [
            {"id": 4,
            "name": "Guns N Petals",
            "genres": ["Rock n Roll"],
            "city": "San Francisco",
            "state": "CA",
            "phone": "326-123-5000",
            "website": "https://www.gunsnpetalsband.com",
            "facebook_link": "https://www.facebook.com/GunsNPetals",
            "seeking_venue": True,
            "seeking_description": "Looking for shows to perform at in the San Francisco Bay Area!",
            "image_link": "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80",
            },
            {"id": 5,
            "name": "Matt Quevedo",
            "genres": ["Jazz"],
            "city": "New York",
            "state": "NY",
            "phone": "300-400-5000",
            "facebook_link": "https://www.facebook.com/mattquevedo923251523",
            "seeking_venue": False,
            "seeking_description": "",
            "image_link": "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80",
            },
            {"id": 6,
            "name": "The Wild Sax Band",
            "genres": ["Jazz", "Classical"],
            "city": "San Francisco",
            "state": "CA",
            "phone": "432-325-5432",
            "facebook_link": "",
            "seeking_venue": False,
            "seeking_description": "",
            "image_link": "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80",
            }
        ]
    )

    op.bulk_insert(
        shows_table,
        [
           {
                "venue_id": 1,
                "artist_id": 4,
                "start_time": "2019-05-21T21:30:00.000Z"
            }, {
                "venue_id": 3,
                "artist_id": 5,
                "start_time": "2019-06-15T23:00:00.000Z"
            }, {
                "venue_id": 3,
                "artist_id": 6,
                "start_time": "2035-04-01T20:00:00.000Z"
            }, {
                "venue_id": 3,
                "artist_id": 6,
                "start_time": "2035-04-08T20:00:00.000Z"
            }, {
                "venue_id": 3,
                "artist_id": 6,
                "start_time": "2035-04-15T20:00:00.000Z"
            }
        ]
    )

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('artists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('genres', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_venue', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('venues',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('genres', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('address', sa.String(length=120), nullable=True),
    sa.Column('city', sa.String(length=120), nullable=True),
    sa.Column('state', sa.String(length=120), nullable=True),
    sa.Column('phone', sa.String(length=120), nullable=True),
    sa.Column('website', sa.String(length=120), nullable=True),
    sa.Column('facebook_link', sa.String(length=120), nullable=True),
    sa.Column('seeking_talent', sa.Boolean(), nullable=True),
    sa.Column('seeking_description', sa.String(), nullable=True),
    sa.Column('image_link', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shows',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artists.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venues.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    seed_data()


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('show')
    op.drop_table('venues')
    op.drop_table('artists')
    # ### end Alembic commands ###
