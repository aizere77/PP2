#AND — BOTH must be True
True and True      # True
True and False     # False
False and True     # False
False and False    # False

temperature = 30
temperature > 20 and temperature < 25
# True and False → False

#OR — AT LEAST ONE must be True
True or True      # True
True or False     # True
False or True     # True
False or False    # False

is_weekend = True
is_holiday = False
is_weekend or is_holiday
# True or False → True

#NOT — flips the Boolean
not True      # False
not False     # True

x = 10
not (x > 5)
# not True → False

x = 7
print((x > 5 and x < 10) or x == 100)

username = "admin"
password = "1234"

username == "admin" and password == "1234"
# True and True → True