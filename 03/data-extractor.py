import dateparser
from price_parser import Price
from schwifty import IBAN

# https://pypi.org/project/dateparser/
# https://pypi.org/project/price-parser/
# https://pypi.org/project/schwifty/

def main():
    d = dateparser.parse('2.Mai 2020', languages=['de'])
    print(d)
    d = dateparser.parse('2.Abc 2020', languages=['de'])
    print(d)
    d = dateparser.parse('2020.12.8')
    print(d)
    print()

    p = Price.fromstring("-114,47 €")
    print(p)
    p = Price.fromstring("3 500 руб")
    print(p)
    p = Price.fromstring("Rs. 11,499")
    print(p)
    p = Price.fromstring("$1499.99")
    print(p)
    p = Price.fromstring("199,999.00")
    print(p)
    p = Price.fromstring("199.999,00")
    print(p)
    print()

    i = IBAN('LT12 1000 0111 0100 1000')
    print(i.country)
    i = IBAN('DE89 3704 0044 0532 0130 00')
    print(i.country)
    try:
        i = IBAN('DE89 3704')
        print(i.country)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()