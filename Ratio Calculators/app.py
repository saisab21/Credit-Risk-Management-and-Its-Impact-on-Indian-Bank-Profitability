from flask import Flask, render_template, request, redirect, url_for
from decimal import Decimal, ROUND_HALF_UP

app = Flask(__name__)

# Function to format values to two decimal places for percentages
def format_percentage(value):
    return float(Decimal(value * 100).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))

# Route for displaying the form and processing the inputs
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Get data from form inputs
            total_debt = float(request.form["total_debt"])
            total_equity = float(request.form["total_equity"])
            non_interest_income = float(request.form["non_interest_income"])
            total_income = float(request.form["total_income"])
            loan_loss_reserves = float(request.form["loan_loss_reserves"])
            gross_loans = float(request.form["gross_loans"])
            net_profit = float(request.form["net_profit"])
            risk_weighted_assets = float(request.form["risk_weighted_assets"])
            tier1_capital = float(request.form["tier1_capital"])
            tier2_capital = float(request.form["tier2_capital"])
            total_deposits = float(request.form["total_deposits"])

            # Optional fields, use default None if not provided
            loan_loss_provisions = request.form.get("loan_loss_provisions", None)
            non_performing_loans = request.form.get("non_performing_loans", None)
            credit_losses = request.form.get("credit_losses", None)
            total_assets = request.form.get("total_assets", None)
            average_earning_assets = request.form.get("average_earning_assets", None)
            average_total_assets = request.form.get("average_total_assets", None)
            average_shareholders_equity = request.form.get("average_shareholders_equity", None)

            # Calculating required ratios
            ratios = {
                "Debt-to-Equity Ratio": total_debt / total_equity,
                "Non-Interest Income to Total Income Ratio (%)": format_percentage(non_interest_income / total_income),
                "Loan Loss Reserve Ratio (%)": format_percentage(loan_loss_reserves / gross_loans),
                "Return on Risk-Weighted Assets (RORWA) (%)": format_percentage(net_profit / risk_weighted_assets),
                "Capital Adequacy Ratio (CAR) (%)": format_percentage((tier1_capital + tier2_capital) / risk_weighted_assets),
                "Credit-to-Deposit Ratio (CDR) (%)": format_percentage(gross_loans / total_deposits),
            }

            # Conditional calculations if optional fields are provided
            if loan_loss_provisions and non_performing_loans:
                ratios["Provision Coverage Ratio (PCR) (%)"] = format_percentage(float(loan_loss_provisions) / float(non_performing_loans))
            if credit_losses and gross_loans:
                ratios["Cost of Risk (%)"] = format_percentage(float(credit_losses) / gross_loans)
            if total_assets and gross_loans:
                ratios["Loan-to-Asset Ratio (%)"] = format_percentage(gross_loans / float(total_assets))
            if average_earning_assets:
                ratios["Net Interest Margin (NIM) (%)"] = format_percentage(net_profit / float(average_earning_assets))
            if non_performing_loans:
                ratios["Gross Non-Performing Assets (GNPA) Ratio (%)"] = format_percentage(float(non_performing_loans) / gross_loans)
            if non_performing_loans and loan_loss_provisions:
                ratios["Net Non-Performing Assets (NNPA) Ratio (%)"] = format_percentage((float(non_performing_loans) - float(loan_loss_provisions)) / gross_loans)
            if average_total_assets:
                ratios["Return on Assets (ROA) (%)"] = format_percentage(net_profit / float(average_total_assets))
            if average_shareholders_equity:
                ratios["Return on Equity (ROE) (%)"] = format_percentage(net_profit / float(average_shareholders_equity))

            # Pass the results to the template
            return render_template("results.html", ratios=ratios)

        except ValueError:
            # Handle invalid input
            return "Please enter valid numerical values."

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
