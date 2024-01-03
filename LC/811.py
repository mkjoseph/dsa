def subdomainVisits(cpdomains):
    domain_count = {}
    for cpdomain in cpdomains:
        count, domain = cpdomain.split()
        count = int(count)
        subdomains = domain.split('.')
        for i in range(len(subdomains)):
            subdomain = '.'.join(subdomains[i:])
            domain_count[subdomain] = domain_count.get(subdomain, 0) + count
    
    result = []
    for subdomain, count in domain_count.items():
        result.append(f"{count} {subdomain}")
    
    return result


# pass 2 

def subdomainVisits(self, cpdomains):
    """
    Counts the number of visits for each subdomain in the given list of domain strings.

    Args:
        cpdomains (list): A list of strings representing the count and domain pairs.

    Returns:
        list: A list of strings representing the count and subdomain pairs.
    """
    count = collections.Counter()
    for cd in cpdomains:
        n, s = cd.split()
        count[s] += int(n)
        for i in range(len(s)):
            if s[i] == '.':
                count[s[i + 1:]] += int(n)
    return ["%d %s" % (count[k], k) for k in count]