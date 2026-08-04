USE CustomerChurnDB;
GO

------------------------------------------------------------
-- 1. Total Customers
------------------------------------------------------------

SELECT COUNT(*) AS TotalCustomers
FROM CustomerChurn;
GO

------------------------------------------------------------
-- 2. Overall Churn Rate
------------------------------------------------------------

SELECT
    Churn,
    COUNT(*) AS CustomerCount,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),2) AS Percentage
FROM CustomerChurn
GROUP BY Churn;
GO

------------------------------------------------------------
-- 3. Customers by Gender
------------------------------------------------------------

SELECT
    Gender,
    COUNT(*) AS TotalCustomers
FROM CustomerChurn
GROUP BY Gender
ORDER BY TotalCustomers DESC;
GO

------------------------------------------------------------
-- 4. Customers by Contract
------------------------------------------------------------

SELECT
    Contract,
    COUNT(*) AS TotalCustomers
FROM CustomerChurn
GROUP BY Contract
ORDER BY TotalCustomers DESC;
GO

------------------------------------------------------------
-- 5. Churn Rate by Contract
------------------------------------------------------------

SELECT
    Contract,

    COUNT(*) AS TotalCustomers,

    SUM(
        CASE
            WHEN Churn='Yes'
            THEN 1
            ELSE 0
        END
    ) AS ChurnedCustomers,

    ROUND(
        SUM(
            CASE
                WHEN Churn='Yes'
                THEN 1
                ELSE 0
            END
        )*100.0/COUNT(*),
        2
    ) AS ChurnRate

FROM CustomerChurn

GROUP BY Contract

ORDER BY ChurnRate DESC;
GO

------------------------------------------------------------
-- 6. Churn Rate by Payment Method
------------------------------------------------------------

SELECT
    PaymentMethod,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS ChurnRate
FROM CustomerChurn
GROUP BY PaymentMethod
ORDER BY ChurnRate DESC;
GO

------------------------------------------------------------
-- 7. Churn Rate by Internet Service
------------------------------------------------------------

SELECT
    InternetService,
    COUNT(*) AS TotalCustomers,
    SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,
    ROUND(
        SUM(CASE WHEN Churn = 'Yes' THEN 1 ELSE 0 END) * 100.0 / COUNT(*),
        2
    ) AS ChurnRate
FROM CustomerChurn
GROUP BY InternetService
ORDER BY ChurnRate DESC;
GO

------------------------------------------------------------
-- 8. Average Monthly Charges by Churn
------------------------------------------------------------

SELECT
    Churn,
    ROUND(AVG(MonthlyCharges), 2) AS AverageMonthlyCharge
FROM CustomerChurn
GROUP BY Churn;
GO

------------------------------------------------------------
-- 9. Average Total Charges by Churn
------------------------------------------------------------

SELECT
    Churn,
    ROUND(AVG(TotalCharges), 2) AS AverageTotalCharge
FROM CustomerChurn
GROUP BY Churn;
GO

------------------------------------------------------------
-- 10. Average Customer Tenure
------------------------------------------------------------

SELECT
    Churn,
    ROUND(AVG(Tenure), 2) AS AverageTenure
FROM CustomerChurn
GROUP BY Churn;
GO

------------------------------------------------------------
-- 11. Revenue by Contract Type
------------------------------------------------------------

SELECT
    Contract,
    COUNT(*) AS Customers,
    ROUND(SUM(TotalCharges), 2) AS TotalRevenue
FROM CustomerChurn
GROUP BY Contract
ORDER BY TotalRevenue DESC;
GO

------------------------------------------------------------
-- 12. Revenue by Internet Service
------------------------------------------------------------

SELECT
    InternetService,
    COUNT(*) AS Customers,
    ROUND(SUM(TotalCharges), 2) AS TotalRevenue
FROM CustomerChurn
GROUP BY InternetService
ORDER BY TotalRevenue DESC;
GO

------------------------------------------------------------
-- 13. Revenue by Payment Method
------------------------------------------------------------

SELECT
    PaymentMethod,
    COUNT(*) AS Customers,
    ROUND(SUM(TotalCharges), 2) AS TotalRevenue
FROM CustomerChurn
GROUP BY PaymentMethod
ORDER BY TotalRevenue DESC;
GO

------------------------------------------------------------
-- 14. Revenue by Gender
------------------------------------------------------------

SELECT
    Gender,
    COUNT(*) AS TotalCustomers,
    ROUND(SUM(TotalCharges),2) AS TotalRevenue,
    ROUND(AVG(TotalCharges),2) AS AverageRevenue
FROM CustomerChurn
GROUP BY Gender
ORDER BY TotalRevenue DESC;
GO

------------------------------------------------------------
-- 15. Revenue by Senior Citizen
------------------------------------------------------------

SELECT
    SeniorCitizen,
    COUNT(*) AS TotalCustomers,
    ROUND(SUM(TotalCharges),2) AS TotalRevenue,
    ROUND(AVG(TotalCharges),2) AS AverageRevenue
FROM CustomerChurn
GROUP BY SeniorCitizen;
GO

------------------------------------------------------------
-- 16. Top 10 Highest Value Customers
------------------------------------------------------------

SELECT TOP 10
    CustomerID,
    Contract,
    PaymentMethod,
    TotalCharges
FROM CustomerChurn
ORDER BY TotalCharges DESC;
GO

------------------------------------------------------------
-- 17. Customer Segmentation
------------------------------------------------------------

SELECT
    CASE
        WHEN TotalCharges < 1000 THEN 'Low Value'
        WHEN TotalCharges < 3000 THEN 'Medium Value'
        ELSE 'High Value'
    END AS CustomerSegment,

    COUNT(*) AS Customers,

    ROUND(AVG(TotalCharges),2) AS AverageRevenue

FROM CustomerChurn

GROUP BY
CASE
    WHEN TotalCharges < 1000 THEN 'Low Value'
    WHEN TotalCharges < 3000 THEN 'Medium Value'
    ELSE 'High Value'
END

ORDER BY AverageRevenue;
GO

------------------------------------------------------------
-- 18. High Risk Customer Segments
------------------------------------------------------------

SELECT
    Contract,
    InternetService,
    PaymentMethod,

    COUNT(*) AS Customers,

    SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,

    ROUND(
        SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),
        2
    ) AS ChurnRate

FROM CustomerChurn

GROUP BY
Contract,
InternetService,
PaymentMethod

HAVING COUNT(*) >= 30

ORDER BY ChurnRate DESC;
GO

------------------------------------------------------------
-- 19. Executive KPI Summary
------------------------------------------------------------

SELECT

COUNT(*) AS TotalCustomers,

SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END) AS ChurnedCustomers,

ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),
2
) AS ChurnRate,

ROUND(AVG(MonthlyCharges),2) AS AverageMonthlyCharge,

ROUND(AVG(TotalCharges),2) AS AverageTotalRevenue,

ROUND(AVG(Tenure),2) AS AverageTenure

FROM CustomerChurn;
GO

------------------------------------------------------------
-- 20. Customer Lifetime Groups
------------------------------------------------------------

SELECT

CASE

WHEN Tenure < 12 THEN 'New'

WHEN Tenure < 36 THEN 'Growing'

WHEN Tenure < 60 THEN 'Loyal'

ELSE 'Long-Term'

END AS CustomerLifetime,

COUNT(*) AS Customers,

ROUND(AVG(TotalCharges),2) AS AverageRevenue,

ROUND(
SUM(CASE WHEN Churn='Yes' THEN 1 ELSE 0 END)*100.0/COUNT(*),
2
) AS ChurnRate

FROM CustomerChurn

GROUP BY

CASE

WHEN Tenure < 12 THEN 'New'

WHEN Tenure < 36 THEN 'Growing'

WHEN Tenure < 60 THEN 'Loyal'

ELSE 'Long-Term'

END

ORDER BY AverageRevenue;
GO