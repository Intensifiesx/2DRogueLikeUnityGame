# Function to get numeric input from the user
def get_input(prompt):
    while True:
        try:
            # Attempt to convert the user input into a float
            return float(input(prompt))
        except ValueError:
            # If conversion fails, inform the user and prompt for input again
            print("Invalid input. Please enter a numeric value.")

# Function to calculate the basic monthly mortgage payment
def calculate_monthly_payment(principal, annual_interest_rate, years):
    # Calculate the monthly interest rate by dividing the annual rate by 12 and converting to a decimal
    monthly_interest_rate = annual_interest_rate / 12 / 100
    # Calculate the total number of payments
    months = years * 12
    # Calculate and return the monthly payment amount using the mortgage formula
    return principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months))

# Function to calculate the total monthly payment including taxes, insurance, and PMI
def calculate_total_monthly_payment(monthly_payment, property_tax, home_insurance, pmi):
    # Add monthly equivalents of property tax, home insurance, and PMI to the basic monthly mortgage payment
    return monthly_payment + (property_tax + home_insurance + pmi) / 12

# Main program execution starts here
print("Mortgage Payment Calculator")

# Collect loan details from the user
principal = get_input("Enter the loan amount (principal): ")
interest_rate = get_input("Enter the annual interest rate (as a percent, e.g., 5 for 5%): ")
years = int(get_input("Enter the loan term in years: "))  # Convert years to integer
property_tax = get_input("Enter the annual property tax: ")
home_insurance = get_input("Enter the annual homeowner's insurance amount: ")
pmi = get_input("Enter the annual Private Mortgage Insurance (PMI) amount if applicable, else enter 0: ")

# Calculate the basic monthly payment without taxes, insurance, or PMI
basic_monthly_payment = calculate_monthly_payment(principal, interest_rate, years)
# Calculate the total monthly payment including taxes, insurance, and PMI
total_monthly_payment = calculate_total_monthly_payment(basic_monthly_payment, property_tax, home_insurance, pmi)

# Display the total monthly mortgage payment to the user
print(f"Your total monthly mortgage payment including taxes, insurance, and PMI will be: ${round(total_monthly_payment, 2)}")
