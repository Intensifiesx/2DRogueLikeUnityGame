def get_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_monthly_interest_rate(annual_interest_rate):
    return annual_interest_rate / 12 / 100

def calculate_monthly_payment(principal, annual_interest_rate, years):
    monthly_interest_rate = calculate_monthly_interest_rate(annual_interest_rate)
    months = years * 12
    return principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months))

def calculate_total_monthly_payment(monthly_payment, property_tax, home_insurance, pmi):
    monthly_property_tax = property_tax / 12
    monthly_home_insurance = home_insurance / 12
    monthly_pmi = pmi / 12
    return monthly_payment + monthly_property_tax + monthly_home_insurance + monthly_pmi


print("Mortgage Payment Calculator")
principal = get_input("Enter the loan amount (principal): ")
interest_rate = get_input("Enter the annual interest rate (as a percent, e.g., 5 for 5%): ")
years = int(get_input("Enter the loan term in years: "))
property_tax = get_input("Enter the annual property tax: ")
home_insurance = get_input("Enter the annual homeowner's insurance amount: ")
pmi = get_input("Enter the annual Private Mortgage Insurance (PMI) amount if applicable, else enter 0: ")

basic_monthly_payment = calculate_monthly_payment(principal, interest_rate, years)
total_monthly_payment = calculate_total_monthly_payment(basic_monthly_payment, property_tax, home_insurance, pmi)

print(f"Your total monthly mortgage payment including taxes, insurance, and PMI will be: ${round(total_monthly_payment, 2)}")
