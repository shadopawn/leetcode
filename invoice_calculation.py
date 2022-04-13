'''
Calculating invoices for customer billing
Background
In the past, we provided some raw billing data in JSON format to the finance team, which they used to manually generate monthly invoices for our customers. Recently, they’ve asked us to create some automation to make this process less error-prone.

Instructions
Your goal is to implement the bill_for function to calculate the total monthly bill for a customer.

Customers are billed based on their subscription tier for the month. We charge them a prorated amount for each user who was active during that month.

You talked with the other engineers on the team and decided that the following algorithm would work:

Calculate a daily rate for the active subscription tier
For each day of the month, identify which users were active that day
Multiply the number of active users for the day by the daily rate to calculate the total for the day
Return the running total for the month at the end, rounded to 2 decimal places
Parameters
This billing function accepts the following parameters:

month
Always present. Has the following structure:

"2019-01"   # January 2019 in YYYY-MM format
active_subscription
May be None. If present, has the following structure:

{
  'id': 1,
  'customer_id': 1,
  'monthly_price_in_dollars': 4  # price per active user per month
}
users
May be empty, but not None. Has the following structure:

[
  {
    'id': 1,
    'name': 'Employee #1',
    'customer_id': 1,

    # when this user started
    'activated_on': datetime.date(2018, 11, 4),

    # last day to bill for user
    # should bill up to and including this date
    # since user had some access on this date
    'deactivated_on': datetime.date(2019, 1, 10)
  },
  {
    'id': 2,
    'name': 'Employee #2',
    'customer_id': 1,

    # when this user started
    'activated_on': datetime.date(2018, 12, 4),

    # hasn't been deactivated yet
    'deactivated_on': None
  }
]
Return value
This function should return the total monthly bill for the customer, rounded to 2 decimal places.

If there are no users or the subscription is not present, the function should return 0 since the customer does not owe anything for that month.

Calculation Examples
Here is an example of calculating the amount to bill each customer using the algorithm described above. This example is captured by the "works when a user is activated during the month" test.

Month	2019-01
Subscription tier	$4 / month
User activations	2018-11-04
2018-12-04
2019-01-10 (new this month)
User deactivations	None
Daily rate is $0.129032258   (this is the monthly rate of $4.00 / 31 days in January) 

2019-01-01  2 active users * $0.129032258 = $0.258064516  (subtotal: $0.258064516)
2019-01-02  2 active users * $0.129032258 = $0.258064516  (subtotal: $0.516129032)
...
2019-01-09  2 active users * $0.129032258 = $0.258064516  (subtotal: $2.322580645)
2019-01-10  3 active users * $0.129032258 = $0.387096774  (subtotal: $2.709677419)
2019-01-11  3 active users * $0.129032258 = $0.387096774  (subtotal: $4.387096772)
...
2019-01-30  3 active users * $0.129032258 = $0.387096774  (subtotal: $10.451612903)
2019-01-31  3 active users * $0.129032258 = $0.387096774  (subtotal: $10.838709677)

Total = $10.84 (round subtotal to nearest cent)
Testing
The automated tests we provide only cover a few key cases, so you should plan to add some of your own tests or modify the existing ones to ensure that your solution handles any edge cases. You should be able to follow the existing patterns for naming and constructing tests to add your own.

Notes / Edge cases
It’s more important for the return value to be correct than it is for the algorithm to be highly optimized.
You can store intermediate results as any kind of decimal type (e.g. float, double). You do not need to round values until the last step.
You should bill for all days between and including both the activation and deactivation dates since the user still had some access on the last day.
You should not change function names or return types of the provided functions since our test cases depend on those not changing.
'''


import unittest
import datetime
from datetime import datetime as dt
import calendar


def bill_for(month, active_subscription, users):
    total = 0
    current_date = dt.strptime(month, "%Y-%m")
    end_of_month = last_day_of_month(current_date)
    daily_rate = calculate_daily_rate(current_date, active_subscription)
    while current_date <= end_of_month:
        current_active_users = active_users(current_date, end_of_month, users)
        total += current_active_users * daily_rate
        current_date = next_day(current_date)
    return round(total, 2)


def calculate_daily_rate(month, active_subscription):
    days_in_month = calendar.monthrange(month.year, month.month)[1]
    monthly_rate = active_subscription["monthly_price_in_dollars"]
    return monthly_rate / days_in_month


def active_users(date, end_of_month, users):
    active_count = 0
    for user in users:
        if "activated_on" not in user:
            continue
        activated_on = user["activated_on"]
        deactivated_on = user["deactivated_on"] if user["deactivated_on"] else end_of_month.date()
        if activated_on <= date.date() <= deactivated_on:
            active_count += 1
    return active_count


def first_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the first day of that month. For example:

    >>> first_day_of_month(datetime.date(2019, 2, 7))  # Feb 7
    datetime.date(2019, 2, 1)                          # Feb 1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date.replace(day=1)


def last_day_of_month(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the last day of that month. For example:

    >>> last_day_of_month(datetime.date(2019, 2, 7))  # Feb  7
    datetime.date(2019, 2, 28)                        # Feb 28

    Input type: datetime.date
    Output type: datetime.date
    """
    last_day = calendar.monthrange(date.year, date.month)[1]
    return date.replace(day=last_day)


def next_day(date):
    """
    Takes a datetime.date object and returns a datetime.date object
    which is the next day. For example:

    >>> next_day(datetime.date(2019, 2, 7))   # Feb 7
    datetime.date(2019, 2, 8)                 # Feb 8

    >>> next_day(datetime.date(2019, 2, 28))  # Feb 28
    datetime.date(2019, 3, 1)                 # Mar  1

    Input type: datetime.date
    Output type: datetime.date
    """
    return date + datetime.timedelta(days=1)


user_signed_up = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 3,
        'name': 'Employee #3',
        'activated_on': datetime.date(2019, 1, 10),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

constant_users = [
    {
        'id': 1,
        'name': 'Employee #1',
        'activated_on': datetime.date(2018, 11, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
    {
        'id': 2,
        'name': 'Employee #2',
        'activated_on': datetime.date(2018, 12, 4),
        'deactivated_on': None,
        'customer_id': 1,
    },
]

new_plan = {
    'id': 1,
    'customer_id': 1,
    'monthly_price_in_dollars': 4
}

no_users = []

# Note: the class must be called Test


class Test(unittest.TestCase):
    def test_works_when_the_customer_has_no_active_users_during_the_month(self):
        self.assertAlmostEqual(
            bill_for('2019-01', new_plan, no_users), 0.00, delta=0.01)

    def test_works_when_everything_stays_the_same_for_a_month(self):
        self.assertAlmostEqual(
            bill_for('2019-01', new_plan, constant_users), 8.00, delta=0.01)

    def test_works_when_a_user_is_activated_during_the_month(self):
        self.assertAlmostEqual(
            bill_for('2019-01', new_plan, user_signed_up), 10.84, delta=0.01)


if __name__ == "__main__":
    unittest.main(verbosity=2)
