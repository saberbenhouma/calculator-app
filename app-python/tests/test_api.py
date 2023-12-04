import unittest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..main import app
from ..models import Base, Calculation


class TestAPI(unittest.TestCase):
    def setUp(self):
        # Création des tables dans la base de données de test
        self.engine = create_engine("sqlite:///:memory:")
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.Session = SessionLocal
        self.session = SessionLocal()
        Base.metadata.create_all(bind=self.engine)

        self.client = TestClient(app)

    def tearDown(self):
        # Suppression des tables de la base de données de test
        Base.metadata.drop_all(bind=self.engine)

    def test_calculate_endpoint(self):
        # Test de l'endpoint /calculate

        response = self.client.post("/calculate", json={"expression": "3 4 +"})

        self.assertEqual(response.status_code, 200)

        self.assertEqual(response.json(), {"result": 7.0})

    def test_export_csv_endpoint(self):
        # Test de l'endpoint /export_csv

        calculation = Calculation(expression="3 4 +", result=7.0)
        self.session.add(calculation)
        self.session.commit()

        response = self.client.get("/export_csv")

        self.assertEqual(response.status_code, 200)

        # Vérifie le contenu du fichier CSV
        lines = response.text.strip().split('\n')
        self.assertEqual(len(lines), 2)  # Vérifie qu'il y a deux lignes (header + data)
        self.assertEqual(lines[0], "Expression,Result")  # Vérifie le header
        self.assertEqual(lines[1], "3 4 +,7.0")  # Vérifie les données

if __name__ == "__main__":
    unittest.main()
