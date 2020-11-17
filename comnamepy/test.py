from get_company_name.comnamepy import get_comname

if __name__ == '__main__':
    company = get_comname.whois_search_company('rc.jp')
    # company = get_comname.get_title('sut.jp')
    print(company)
