import whois
import re
import requests
from bs4 import BeautifulSoup


# Get company name from whois


def whois_search_company(domain):
    try:
        # Get domain information from whois
        whois_domain = whois.whois(domain)
    except:
        return print('No match domain!!!')

    # Make a dictionary in the domain information
    domain_dict = whois_domain.__dict__

    # Get company name from text

    try:
        # co.jp
        if domain.endswith('co.jp'):
            # Get the index before and after the company name
            org_index = domain_dict['text'].split().index('[組織名]')
            end_org_index = domain_dict['text'].split().index('g.')
            # Get between org_index and end_org_index
            org_name = domain_dict['text'].split()[org_index + 1: end_org_index]
        # .jp
        elif domain.endswith('jp'):
            # Get the index before and after the company name
            org_index = domain_dict['text'].split().index('[登録者名]')
            end_org_index = domain_dict['text'].split().index('[Registrant]')
            # Get between org_index and end_org_index
            org_name = domain_dict['text'].split()[org_index + 1: end_org_index]
        # other
        else:
            # Get index of Admin Organization
            org_index = re.split('[,:\n]', domain_dict['text']).index(
                'Admin Organization')
            # Get the company name in the index next to org_index
            org_name = re.split('[,:\n]', domain_dict['text'])[org_index + 1]
    except:
        # If there is no organization name or registrant name, Admin Organization
        return print('not found company name')

    # Replace \ n and \ r with spaces
    org_name = ''.join(org_name).translate(str.maketrans({'\n': '', '\r': ''}))

    # Returns the company name
    return org_name



# Scraping at 「https: //」, 「https: // www.」, 「http: //」, 「http: // www.」
def get_title(domain):

    # Prepare search URL
    url_https = 'https://' + domain
    url_https_www = 'https://www.' + domain
    url_http = 'http://' + domain
    url_http_www = 'http://www.' + domain

    # Create a list of URLs
    url_list = (url_https, url_https_www, url_http, url_http_www)

    #　Turn url_list to search one by one
    for url in url_list:
        try:
            # Visit page
            response = requests.get(url)
        except:
            continue
        # If you can get the contents of the URL, you can exit
        break
    # When you can't get the URL
    else:
        return print('not found url')


    # Measures against garbled characters
    response.encoding = response.apparent_encoding
    # Get HTML
    bs = BeautifulSoup(response.text, 'html.parser')
    # Get the title
    try:
        title = bs.title.string
    except:
        return print('not found title')

    # Remove whitespace
    title = str(title).replace(' ', '')
    return title

def main():
    company_name = whois_search_company('taktpixel.co.jp')
    print(company_name)

if __name__=='__main__':
    main()


