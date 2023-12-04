#!/usr/bin/env python3
"""sends a request to the URL and displays the request id in the header of the response
"""
import urllib.request
import sys
if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(request) as response:
        print(response.getheader("X-Request-Id"))
