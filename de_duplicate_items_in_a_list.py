#
# www.youtube.com/@mersthub_mentors
#

my_items = ["duck", "goose", "goose", "cat"]

# without maintaining order of items
unique_items = set(my_items)
print(f"Without maintaining order:\n{unique_items}")

# maintaining order of items
unique_items = list(dict.fromkeys(my_items))
print(f"\nMaintaining order of items:\n{unique_items}")
