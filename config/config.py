class Config:
    SQLALCHEMY_DATABASE_URI = (
        "mssql+pyodbc://@DESKTOP-LQC3MB2\\SQLEXPRESS/TALLER_1_MODULO_3?"
        "driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
    )

    SECRET_KEY = 'd40449bf-d7f1-4a01-9950-ff56e70fece453b6a16b-726d-45cf-b083-0a7a11784905ae25155e-ced1-4ed0-92d6-6b4dedc5c663'