import re
# TODO: Perhaps rename function from cleanURL to fetchID??

# This function is passed an Amazon URL and returns the unique ID for a given Amazon Product
def cleanURL(url):
    # We search for the ID start of a given URL
    match = re.search("dp/..........|gp/product/..........|gp/video/detail/..........", url)
    if match:
        # Assign 'short' to the index of the re.search
        short = match.group(0)
        # Split 'short' by '/'
        id = short.split('/')
        # print(id)
        if(id[1] == 'product'):
            return id[2]
        if(id[1] == 'video'):
            return id[3]
        # Return the ID
        return id[1]

    # Return error otherwise
    return "ID Scrape Error"


