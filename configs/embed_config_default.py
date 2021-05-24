# Rules are created and sorted in the order that they are inserted in the code
rules = [
    # Format is [Str: Rule, Str: Rule Description, Bool: Inline]
    # Add a comma in between each rule.
    # Eg ['rule-1', 'Don't Do This', False],
    # Eg ['rule-2', 'Do This', False]
]

# Servers are created and sorted in the order that they are inserted in the code
servers = [
    # Format is [Str: Server Name, Str: Server Description, Bool: Inline]
    # ['Flex Server', 'Our Website And Hosting at https://greyscorp.herokuapp.com/', False],
    # ['Github', 'Our Github Page At https://github.com/GreyStinger/Flex-Discord-Bot', True]
]

# Static builds need their own list item in the same formatting as what the current ones are.
# Add the aliases that you want the embed to be called with at the end of the list.
# Comment out the current items if necessary
# Static Builds:
STATIC_BUILDS = {
    'Rules': ['Please Read These Carefully', rules],
    'Servers': ['These are our currently hosted servers.', servers]
}


# Anything after this please ignore as it wont affect you.

def name_builder():
    item_list = []
    for key in STATIC_BUILDS:
        item_list.append(key.lower())
    return item_list


STATIC_NAMES = name_builder()
