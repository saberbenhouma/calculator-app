from fastapi.responses import StreamingResponse
import csv
from sqlalchemy.orm import Session
from models import Calculation

def export_to_csv():
    session = Session()
    calculations = session.query(Calculation).all()

    response = StreamingResponse(content_type="text/csv")
    response.headers["Content-Disposition"] = 'attachment; filename="calculations.csv"'

    writer = csv.writer(response.iter_lines())
    writer.writerow(["Expression", "Result"])

    for calculation in calculations:
        writer.writerow([calculation.expression, calculation.result])

    return response
