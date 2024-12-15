import string, random

def generage_tracking_number(prefix='WXYZ', sections=3, section_length=4):
    part = [
        ''.join(random.choices(string.ascii_uppercase + string.digits, k=section_length)) for _ in range(sections)
    ]
    
    return f"{prefix}-{'-'.join(part)}"
    

print(generage_tracking_number())