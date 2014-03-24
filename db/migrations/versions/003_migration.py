from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()

message = Table('message', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=100)),
    Column('text', Text),
    Column('timestamp', DateTime),
    Column('unread', Boolean, default=ColumnDefault(True)),
    Column('user_id', Integer, ForeignKey('user.id'), nullable=False),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    
    # Gotta create that, or else it won't find 'user' in the foreign key
    user = Table('user', post_meta, autoload=True,
                 autoload_with=migrate_engine)
    
    post_meta.tables['message'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['message'].drop()
