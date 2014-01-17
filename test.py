import adnpy

# Set the default access token for API calls.
adnpy.api.add_authorization_token('AUTH_TOKEN')

# Send a broadcast with the BroadcastMessageBuilder recipe.
builder = adnpy.recipes.BroadcastMessageBuilder(adnpy.api)
builder.channel_id = 12345 # Get this channel ID from the web publisher tools
builder.headline = 'Hello World!'
builder.text = 'Sending this from [ADNPy](https://github.com/appdotnet/ADNPy) was easy!'
builder.parse_markdown_links = True
builder.read_more_link = 'http://adnpy.readthedocs.org/'
builder.send()
