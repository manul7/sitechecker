import time
import requests
import re

# This can be moved to a config file, but for simplicity it's here
PRECISION = 6


def check_site(url, pattern=None):
    """Check if a website is available and if the content matches a regex pattern.
    :param url: The URL of the website to check.
    :param pattern: The regex pattern to match.
    :return: A tuple containing the response time, the status code and a boolean indicating
    if the regex pattern matched."""

    regex_matched = False

    start_time = time.time()
    # Make a request to the target website
    response = requests.get(url)
    # Collect metrics
    response_time = round(time.time() - start_time, PRECISION)
    status_code = response.status_code

    if pattern:
        result = re.search(pattern, response.text)
        regex_matched = bool(result)

    return response_time, status_code, regex_matched
