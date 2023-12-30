import re
def mask_personal_info(s):
    if re.match(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$', s):
        # Mask email address
        name, domain = s.split('@')
        masked_name = name[0] + '*****' + name[-1]
        masked_domain = domain[0] + '*****' + domain[-1]
        masked_email = masked_name.lower() + '@' + masked_domain.lower()
        return masked_email
    elif re.match(r'^[\d+\-() ]+$', s):
        # Mask phone number
        digits = re.sub(r'\D', '', s)
        local_number = digits[-10:]
        country_code = digits[:-10]
        masked_local_number = '***-***-' + local_number[-4:]
        if country_code:
            masked_phone_number = '+' + '*' * len(country_code) + '-' + masked_local_number
        else:
            masked_phone_number = masked_local_number
        return masked_phone_number
    else:
        return "Invalid personal information"

# Example usage
personal_info = "john.doe@example.com"
masked_info = mask_personal_info(personal_info)
print(masked_info)
