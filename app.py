"""Main application module for handling web requests."""

import os

from flask import Flask


def create_app():
    """
    Create and configure an instance of the Flask application.

    Returns:
        web_app: An instance of the Flask application.
    """
    web_app = Flask(__name__)
    web_app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),  # Use environment variable
        DEBUG=False,  # Disable debug mode in production
        SQLALCHEMY_DATABASE_URI='sqlite:///your_database.db',
    )
    return web_app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=False)
