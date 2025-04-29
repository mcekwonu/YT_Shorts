#
# www.youtube.com/@mersthub_mentors
#

# if role == "admin ":
#    print("Welcome, Admin!")
# elif role == "user":
#    print(f"You are user 1")


from enum import Enum

class Role(Enum):
    ADMIN = "admin"
    USER = "user"
    GUEST = "guest"


role = Role.ADMIN

if role == Role.ADMIN:
    print("\nWelcome, admin!")
