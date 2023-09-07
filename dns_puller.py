import dns.resolver


result = dns.resolver.resolve('dnspython.org', 'MX')
for ipval in result:
    print('Host', ipval.exchange, 'has preference', ipval.preference)
    