from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Calculation
from calculations import evaluate_npi
from export import export_to_csv
import uvicorn

app = FastAPI()

# Configuration de la Data Base
engine = create_engine("sqlite:///./test.db")
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Endpoint pour calculer une expression

@app.options("/calculate")
async def options_calculate():
    return {"Allow": "POST"}

@app.post("/calculate")
def calculate(expression: str):
    result = evaluate_npi(expression)

    # Enregistrement dans la Data Basee
    session = SessionLocal()
    db_calculation = Calculation(expression=expression, result=result)
    session.add(db_calculation)
    session.commit()

    return {"result": result}

# Endpoint pour exporter les données au format CSV
@app.get("/export_csv")
def export_csv():
    return export_to_csv()


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
