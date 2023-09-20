# Assignment 1
"""1. Print out the following text:
I would like to analyze the following company: [insert a company name].
Download historical data and trade based on algorithms.
"""
input(print('I would like to analyze the following compnay: ')


"""2. Change these strings so that they print out properly.
print('Google's not even that profitable!')
print("What's the meaning of "quantitative trading"?")
"""
print("Google's not even that profitable!")
print("What's the meaning of quantitative trading?")

"""3. Create variables to store a company's name, ticker, the index it trades on,
its current stock price, latest daily return, and market cap.
Then print them out.
"""
company_name = "Google"
company_ticker = "GOOGL"
index_traded_on = "XYZ"
current_stock_price = 100.50
latest_daily_return = 0.025
market_cap = 9000000000
print("Company Name:", company_name)
print("Ticker:", company_ticker)
print("Index Traded On:", index_traded_on)
print("Current Stock Price:", current_stock_price)
print("Latest Daily Return:", latest_daily_return)
print("Market Cap:", market_cap)


"""4. Compute the total amount to pay for a stock if yesterday it was priced at $12.34,
it had a price increase of 1.21%, and you need to pay the broker $0.09 for fees.
Store the result in a variable named total.
"""
recent_price = 12.34
price_increase = 1.21/100
broker_fee = 0.09
total_amount = (recent_price + (recent_price * price_increase)) + broker_fee
print(total_amount)

"""5. Do the following:
Take the string "1.21%" and strip off the percent sign.
Convert it into a number.
Divide it by 100.
Print out the result.
"""
string = "1.21%"
number = float(string.strip("%"))
print(number / 100)



"""6. Use input() to ask a user for a company they like, and then print it out in:
- Uppercase
- Lowercase
- Title case
"""
company_name = input(print("what is your favourite company? "))
print(company_name.upper())
print(company_name.lower())
print(company_name.title())


"""7. Build a future value calculator by using input() to get values from the user.
(Make sure you convert them into integers or floats before doing any math on them.)
Print out the result.
Hint: Future Value = Present Value x (1 + Rate of Return) ^ Number of Periods"""
present_value = float(input"Enter present value: "))
rate_of_return = float(input("Enter rate of return: "))
number_of_period = float(input("Enter number of period: "))
future_value = present_value * (1 + rate_of_return ^ number_of_period)
print(future_value)


"""8. Write an if statement that checks the credentials given by a user.
If the username is "admin" and the password is "123456" print
a message indicating success, otherwise print that the username and/or password
is incorrect. The username should not be case sensitive.
username = input("Username: ")
password = input("Password: ")"""

username = input("Username: ")
password = input("password: ")
if username.lower == "admin" and password == "123456":
    print("Success")
else:
    print("Username or password incorrect")



"""9. Create three different lists containing:
- Your top 3 publicly traded companies
- The most recent stock price for your three companies
- The percentage stock return for the last day for each of your three companies"""
companies = ["A", "B", "C"]
stock_prices = [100.50, 50.25, 75.75]
stock_returns = [0.025, -0.01, 0.015]


"""10. Go through the lists you created above and use list indexes []
to print out the following from each list:
- Your favorite company
- The lowest price of your three companies
- The highest daily return of your three companies
Compare the last two to the results you get using the min() and max() functions."""
companies = ["A", "B", "C"]
stock_prices = [100.50, 50.25, 75.75]
stock_returns = [0.025, -0.01, 0.015]
print("My fav company is ", companies[0])
lowest_price = stock_prices[1]
highest_return = stock_return[0]
print("The lowest price of the three companies is ", lowest_price)
print("The highest daily return of the company is ", highest_return)
if lowest_price == min(stock_prices) and highest_return == max(stock_returns):
    print("True")
else:
    print("false")

"""11. Write an if statement that loops over each number in the daily_returns list
and prints out whether it is positive or negative."""

daily_returns = [.0015, .0112, -.0012, .0239, .0039, -.0059, -.0081, .0132, .0021]

count = 0
while count < 0
daily_returns = daily_returns[0]
if daily_returns[0] < 0:
    print(Negative)
    else print("Positive")
count +=1

print("end of loop")





"""12. Convert the companies string into a list using split()
and save it into the companies variable."""

companies = "Microsoft, Kraft Heinz, Facebook, Comcast Corporation, Apple"
name = companies.split()
print(name)

"""13. Using a for loop to loop over the list of companies created above, take the companies
whose names are less than 10 characters long and append them to a new list."""


"""14. Use join() to print out the new list of short companies you created above as a string
with commas in between each one."""
