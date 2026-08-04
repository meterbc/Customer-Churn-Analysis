from sqlalchemy import create_engine
from sqlalchemy import text

SERVER = r"Mete\SQLEXPRESS"
DATABASE = "CustomerChurnDB"

connection_string = (
    f"mssql+pyodbc://@{SERVER}/{DATABASE}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&trusted_connection=yes"
    "&TrustServerCertificate=yes"
)

engine = create_engine(connection_string)

try:
    with engine.connect() as connection:
        result = connection.execute(text("SELECT @@VERSION"))

        print("=" * 60)
        print("CONNECTED TO SQL SERVER")
        print("=" * 60)

        print(result.scalar())

except Exception as e:
    print(e)