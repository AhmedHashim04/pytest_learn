
def get_full_name(first, last, middle=""):
    """Return the full name of a person."""
    if middle:
        name = f"{first} {middle} {last}"
    else:
        name = f"{first} {last}"
    return name.title()

