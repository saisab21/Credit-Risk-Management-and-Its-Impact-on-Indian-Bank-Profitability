# Credit Risk Management and Its Impact on Indian Bank Profitability

## Project Overview
This project investigates the relationship between credit risk management and profitability among Indian banks, using various financial ratios and metrics to measure risk exposure, capital adequacy, profitability, and operational efficiency. By calculating these key metrics, we aim to identify trends and draw insights into how effective credit risk management contributes to the financial health and profitability of banks.

**This project is part of the Money, Banking, and Finance course at IISER Bhopal. For any queries, please contact saisab21@iiserb.ac.in / ashim21@iiserb.ac.in**

## Objectives
- **To analyze the financial health and credit risk exposure of Indian banks.**
- **To calculate and interpret key financial ratios and metrics.**
- **To understand the impact of credit risk management on bank profitability.**

## Key Financial Ratios and Metrics
The following essential financial ratios and metrics are used to assess the credit risk profile and profitability of banks:

### Essential Ratios
1. **Debt-to-Equity Ratio**: Measures a bank's leverage by comparing total debt to total equity, indicating the extent of borrowing relative to owned capital.
2. **Non-Interest Income to Total Income Ratio**: Indicates the percentage of a bank’s revenue from non-interest sources, showing diversification of income.
3. **Loan Loss Reserve Ratio**: Reflects the percentage of loans covered by reserves, a measure of risk mitigation against potential defaults.
4. **Return on Risk-Weighted Assets (RORWA)**: Assesses the return generated on assets that are adjusted for risk, providing a profitability perspective.
5. **Capital Adequacy Ratio (CAR)**: Shows a bank’s capacity to absorb losses, comparing its capital with risk-weighted assets.
6. **Credit-to-Deposit Ratio (CDR)**: Reveals the portion of deposits used for lending, an indicator of liquidity and risk-taking.

### Optional Ratios (if data is available)
1. **Provision Coverage Ratio (PCR)**: Measures the coverage of non-performing assets by provisions, reflecting risk management adequacy.
2. **Cost of Risk**: Calculated as the ratio of credit losses to total loans, showing the financial impact of risk.
3. **Loan-to-Asset Ratio**: Indicates the proportion of assets in the form of loans, assessing risk exposure in the bank’s asset base.
4. **Net Interest Margin (NIM)**: Assesses profitability by comparing interest income from loans with interest expenses.
5. **Gross Non-Performing Assets (GNPA) Ratio**: Shows the percentage of loans that are non-performing, a key measure of asset quality.
6. **Net Non-Performing Assets (NNPA) Ratio**: Adjusts the GNPA for provisions, showing uncovered non-performing assets.
7. **Return on Assets (ROA)**: Measures overall profitability relative to total assets, showing efficiency in asset usage.
8. **Return on Equity (ROE)**: Indicates profit generated per unit of shareholder equity, showing efficiency and profit potential.

## Data Collection
Most of these metrics can be calculated using data from financial statements, including balance sheets and income statements, typically found in annual reports or other public filings of Indian banks. The following inputs are generally required:
- Total Debt, Total Equity, Non-Interest Income, Total Income, Loan Loss Reserves, Gross Loans, Net Profit, Risk-Weighted Assets, Tier 1 and Tier 2 Capital, Total Deposits, etc.

Optional inputs include Provision Amounts, Non-Performing Loans, Credit Losses, and Total Assets. 

The dataset on which the analysis is done can be accessed at [https://docs.google.com/spreadsheets/d/1HmwqxtZMcYe_jRyo2PxIw6qX6fPE0EVgBDo3v_EowDA/edit?usp=sharing](url)

## Analysis Approach
The analysis process involves:
1. **Data Collection**: Gather the basic input metrics from publicly available financial statements for selected banks.
2. **Ratio Calculations**: Using the inputs, calculate each of the financial ratios as outlined above.
3. **Interpretation**: Interpret the results for each bank, focusing on:
   - **Risk Exposure**: Metrics like Loan Loss Reserve Ratio, GNPA, and NNPA ratios will indicate credit risk levels.
   - **Capital Adequacy**: CAR and Debt-to-Equity Ratio provide insights into capital sufficiency and leverage.
   - **Profitability**: Metrics like ROA, ROE, and NIM highlight how efficiently banks generate profit relative to risk exposure.
4. **Comparative Analysis**: Compare metrics across multiple banks to identify patterns and outliers in credit risk management and profitability.
5. **Insights and Recommendations**: Based on the analysis, derive insights into how credit risk impacts bank profitability and provide recommendations for effective risk management.

## How to Use This Repository
1. **Input Financial Data**: Gather data for each bank, particularly the essential fields needed for ratio calculations.
2. **Run Calculations**: Use the provided code to calculate ratios based on the inputs.
3. **Analyze Results**: Compare calculated metrics across banks and interpret them to understand the impact of credit risk on profitability.
4. **Contribute**: You’re welcome to improve or expand this project with new metrics, data sources, or analysis methods.

## Dependencies
The code relies on Python and requires basic libraries like `Flask` (for the web interface) and `decimal` for precise ratio calculations. Detailed installation instructions are provided in the code files.

## Future Enhancements
- **Automation of Data Collection**: Incorporating APIs or web scraping to pull data automatically.
- **Additional Ratios**: Expand analysis with more metrics as per evolving financial reporting standards.
- **Visualization**: Add data visualization for trends and comparisons to improve interpretability.

## License
This project is open-source and citations welcomed.
