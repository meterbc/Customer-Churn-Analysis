USE CustomerChurnDB;
GO

IF OBJECT_ID('CustomerChurn', 'U') IS NOT NULL
    DROP TABLE CustomerChurn;
GO

CREATE TABLE CustomerChurn
(
    CustomerID VARCHAR(20) PRIMARY KEY,
    Gender VARCHAR(10),
    SeniorCitizen BIT,
    Partner VARCHAR(3),
    Dependents VARCHAR(3),
    Tenure INT,
    PhoneService VARCHAR(3),
    MultipleLines VARCHAR(25),
    InternetService VARCHAR(20),
    OnlineSecurity VARCHAR(25),
    OnlineBackup VARCHAR(25),
    DeviceProtection VARCHAR(25),
    TechSupport VARCHAR(25),
    StreamingTV VARCHAR(25),
    StreamingMovies VARCHAR(25),
    Contract VARCHAR(30),
    PaperlessBilling VARCHAR(3),
    PaymentMethod VARCHAR(50),
    MonthlyCharges DECIMAL(10,2),
    TotalCharges DECIMAL(10,2),
    Churn VARCHAR(3)
);
GO