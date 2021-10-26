An API built with FastAPI, SQLAlchemy, Postgresql and docker


STEPS: 

    venv: 
        python -m venv venv 
        source venv/bin/activate
        pip install -r requirements.txt
        
    run-db:
        docker-compose up -d (if it fails, try to run with sudo)

    create-database:
        python src/database.py

    start-api:
        uvicorn src.main:app --reload
