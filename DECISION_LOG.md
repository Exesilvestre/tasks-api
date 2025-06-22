## Technical Decisions

- We use **PostgreSQL** because it is a robust and reliable relational database that works very well with FastAPI. It offers strong support for SQLAlchemy and async operations, making it a solid choice for data integrity and complex queries.

- We follow a **Clean Architecture** pattern, dividing the project into three layers: Domain, Application, and Infrastructure. This keeps responsibilities clearly separated, making the codebase cleaner, easier to maintain, and more scalable.

- The database connection is implemented as a **singleton** to ensure only one connection pool is used throughout the application. This improves performance by reusing connections and helps prevent connection leaks.

- We use **Alembic** for managing database migrations. It allows us to track and version changes to the database schema over time, making it easier to keep development, testing, and production environments in sync.

- In our **Flake8 configuration**, we ignore a few specific rules to improve code readability and flexibility during development:
  - `E501` (line too long): We prefer slightly longer lines (up to 88 chars) for better clarity, especially in SQLAlchemy models and route definitions.
  - `F401` (imported but unused): We ignore this in some files where imports are required for side effects (like Alembic or FastAPI routers).
  - `F403` (from module import *): Ignored where necessary, for example, when importing all routes for simplicity in `__init__.py`.

## Pendings and improvements
I will add a User table and protect the endpoints using authentication with tokens and login endpoints. I’ve already implemented integration tests to ensure that the components work correctly together. While I still need to develop more unit tests in the future, I prioritized integration tests due to time constraints, as they provide broader coverage of the application.

Additionally, it would be more efficient to define fixtures at the beginning of the test suite and reuse that data across tests, instead of creating new entities within each test.

For security, I plan to follow the approach described in the official FastAPI documentation on OAuth2 with Password (and hashing), Bearer with JWT tokens. This includes hashed passwords, access tokens, and refresh tokens. As an improvement, adding a middleware to validate the user's identity on each request would be a good practice to strengthen security.