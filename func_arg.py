# def user_info(name, age=0,city="Tucson"):
#     '''
#     This funtion prints the name, age, and cuty
#     from and argument provided to the function.
#     '''

#     print("{} is {} years old, from {}".format(name, age, city))

# user_info("Rizwan", 35, "new york")
# user_info("Micah")
# user_info(age=56, name="rima")

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. His email is {} and his salary is {}".format(fname, lname,
    company, email, *args, **kwargs))

application("Rizwan", "Shaik", "mail@email.com",
    "teachcode.org", 75000, hire_date = "January 2025")