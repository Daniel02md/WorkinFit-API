from flask_migrate import Migrate
from models import app, db
from models.Aluno import Aluno
from models.Professor import Professor

migrate = Migrate(app=app, db=db, command="alembic")