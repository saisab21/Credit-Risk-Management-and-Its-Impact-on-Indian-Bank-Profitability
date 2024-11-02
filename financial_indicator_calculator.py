# Importing the Decimal library for rounding percentages to two decimal places
from decimal import Decimal, ROUND_HALF_UP

# Function to format values into two-decimal-place percentages
def format_percentage(value):
    return float(Decimal(value * 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

# Input dialogue box for entering base values available in public financial documents
print("Please enter the following basic financial metrics from balance sheets and income statements.")

# Collecting essential inputs with explanations on where to find them
# Most inputs below are essential; the comments specify which ones are optional

# Essential financial inputs
total_debt = float(input("Enter Total Debt (in Crores, usually under liabilities in balance sheet): "))
total_equity = float(input("Enter Total Equity (in Crores, available under shareholder's equity): "))
non_interest_income = float(input("Enter Non-Interest Income (in Crores, find in income statement): "))
total_income = float(input("Enter Total Income (in Crores, find in income statement): "))
loan_loss_reserves = float(input("Enter Loan Loss Reserves (in Crores, balance sheet under provisions): "))
gross_loans = float(input("Enter Gross Loans (in Crores, can be found in notes on assets): "))
net_profit = float(input("Enter Net Profit (in Crores, from income statement): "))
risk_weighted_assets = float(input("Enter Risk-Weighted Assets (in Crores, from capital adequacy section): "))
tier1_capital = float(input("Enter Tier 1 Capital (in Crores, available in capital adequacy disclosures): "))
tier2_capital = float(input("Enter Tier 2 Capital (in Crores, under regulatory capital data): "))
total_deposits = float(input("Enter Total Deposits (in Crores, usually in liabilities): "))

# Optional inputs - can be skipped if unavailable; they mainly refine certain ratios
loan_loss_provisions = float(input("Enter Loan Loss Provisions (in Crores, for PCR; find in provisions section): "))
non_performing_loans = float(input("Enter Non-Performing Loans (in Crores, for PCR, GNPA; available in asset quality data): "))
credit_losses = float(input("Enter Credit Losses (in Crores, cost of risk; may be in notes or provisions): "))
total_assets = float(input("Enter Total Assets (in Crores, available on balance sheet): "))
average_earning_assets = float(input("Enter Average Earning Assets (in Crores, for NIM; could use total assets if unavailable): "))
average_total_assets = float(input("Enter Average Total Assets (in Crores, for ROA; could use total assets): "))
average_shareholders_equity = float(input("Enter Average Shareholder's Equity (in Crores, for ROE; could use total equity): "))

# Calculating important metrics based on inputs
ratios = {
    "Debt-to-Equity Ratio": total_debt / total_equity,
    "Non-Interest Income to Total Income Ratio (%)": format_percentage(non_interest_income / total_income),
    "Loan Loss Reserve Ratio (%)": format_percentage(loan_loss_reserves / gross_loans),
    "Return on Risk-Weighted Assets (RORWA) (%)": format_percentage(net_profit / risk_weighted_assets),
    "Capital Adequacy Ratio (CAR) (%)": format_percentage((tier1_capital + tier2_capital) / risk_weighted_assets),
    "Credit-to-Deposit Ratio (CDR) (%)": format_percentage(gross_loans / total_deposits),
}

# Additional metrics if optional data is available
if loan_loss_provisions and non_performing_loans:
    ratios["Provision Coverage Ratio (PCR) (%)"] = format_percentage(loan_loss_provisions / non_performing_loans)

if credit_losses and gross_loans:
    ratios["Cost of Risk (%)"] = format_percentage(credit_losses / gross_loans)

if total_assets and gross_loans:
    ratios["Loan-to-Asset Ratio (%)"] = format_percentage(gross_loans / total_assets)

if average_earning_assets:
    ratios["Net Interest Margin (NIM) (%)"] = format_percentage(net_profit / average_earning_assets)

if non_performing_loans:
    ratios["Gross Non-Performing Assets (GNPA) Ratio (%)"] = format_percentage(non_performing_loans / gross_loans)

if non_performing_loans and loan_loss_provisions:
    ratios["Net Non-Performing Assets (NNPA) Ratio (%)"] = format_percentage((non_performing_loans - loan_loss_provisions) / gross_loans)

if average_total_assets:
    ratios["Return on Assets (ROA) (%)"] = format_percentage(net_profit / average_total_assets)

if average_shareholders_equity:
    ratios["Return on Equity (ROE) (%)"] = format_percentage(net_profit / average_shareholders_equity)

# Displaying calculated ratios and metrics in a clear format
print("\nCalculated Ratios and Metrics:")
for ratio_name, value in ratios.items():
    print(f"{ratio_name}: {value}%")

