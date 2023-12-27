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
        count = collections.Counter()
        for cd in cpdomains:
            n, s = cd.split()
            count[s] += int(n)
            for i in range(len(s)):
                if s[i] == '.':
                    count[s[i + 1:]] += int(n)
        return ["%d %s" % (count[k], k) for k in count]