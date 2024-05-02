from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic.config import Config as AlembicConfig
from alembic import context

# To import models from models.py, we need to append the parent directory to sys.path
import os
import sys
sys.path.append(os.getcwd())  # Assuming alembic/env.py is one level below the project root

from models import Base  # Now we can import models directly

# this is the Alembic Config object, which provides
# access to the values within the .ini file in use.
alembic_cfg = AlembicConfig()

# Check if url attribute exists before using it
if hasattr(alembic_cfg, 'url') and alembic_cfg.url:
    # Interpret the config file for Python logging.
    # This line sets up loggers basically.
    fileConfig(alembic_cfg.config_file_name)

# add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
# 
target_metadata = Base.metadata

def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    if hasattr(alembic_cfg, 'url') and alembic_cfg.url:
        url = alembic_cfg.url
        with context.begin_transaction():
            context.run_migrations()

def run_migrations_online() -> None:
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    if hasattr(alembic_cfg, 'url') and alembic_cfg.url:
        connectable = engine_from_config(
            alembic_cfg.get_section(alembic_cfg.config_ini_section, {}),
            prefix="sqlalchemy.",
            poolclass=pool.NullPool,
        )

        with connectable.connect() as connection:
            context.configure(
                connection=connection, target_metadata=target_metadata
            )

            with context.begin_transaction():
                context.run_migrations()

run_migrations_offline()
run_migrations_online()
