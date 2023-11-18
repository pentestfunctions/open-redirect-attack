import requests
from requests.exceptions import ConnectionError, HTTPError, Timeout, RequestException, SSLError
import urllib3
import urllib.parse

# Disable warnings for SSL issues
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Target URL and the parameter susceptible to open_redirect
url = input("What is the target URL?: ")

# File containing open_redirect payloads
payload_file = "payloads.txt"

# Relevant HTTP response codes
relevant_codes = [301, 302, 307, 308]

def test_open_redirect(url, payload):
    try:
        # Check if the payload is already encoded
        if urllib.parse.unquote(payload) == payload:
            # If not encoded, encode the payload
            encoded_payload = requests.utils.quote(payload)
        else:
            # If already encoded, use as is
            encoded_payload = payload

        full_url = f"{url}{encoded_payload}"
        response = requests.get(full_url, timeout=10, allow_redirects=False, verify=False)

        final_url = response.url

        # Check for both status code and other indications in the response
        if response.status_code in relevant_codes or "some_indicator" in response.text:
            return True
        else:
            return False
    except (ConnectionError, HTTPError, Timeout) as e:
        pass
        return False
    except SSLError as e:
        pass
        return False
    except RequestException as e:
        pass
        return False


def main():
    potential_open_redirect_urls = []  # List to store URLs of potential open_redirects
    max_open_redirect_count = 5  # Maximum number of open_redirects to find before stopping

    with open(payload_file, 'r') as file:
        for line in file:
            payload = line.strip()
            if test_open_redirect(url, payload):
                full_url = f"{url}{requests.utils.quote(payload)}"
                print(f"Potential open redirect found with payload: {payload}")
                potential_open_redirect_urls.append(full_url)

                # Check if the maximum count has been reached
                if len(potential_open_redirect_urls) >= max_open_redirect_count:
                    break

    # Print the summary if any potential open_redirects were found
    if potential_open_redirect_urls:
        print("Scanning stopped due to 5 potential redirects found:")
        print("Full URLs:")
        for open_redirect_url in potential_open_redirect_urls:
            print(open_redirect_url)

if __name__ == "__main__":
    main()

