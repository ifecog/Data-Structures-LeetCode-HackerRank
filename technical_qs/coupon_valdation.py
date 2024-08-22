def coupon_validation(listings):
    corrected_data = []
    
    for listing in listings:
        if listing['coupon_code'] != '':
            listing['final_fare'] = round(listing['fare'] - ((listing['discount_percentage'] / 100) * listing['fare']))
        else:
            listing['final_fare'] = listing['fare']
        
        corrected_data.append(listing)
    
    return corrected_data

# Example usage:
fares = [
  {"id": "1", "coupon_code": "SUMMER21", "fare": 50, "discount_percentage": 20},
  {"id": "2", "coupon_code": "WINTER21", "fare": 100, "discount_percentage": 50},
  {"id": "3", "coupon_code": "", "fare": 75, "discount_percentage": 0}
]


adjusted_fares = coupon_validation(fares)
print(adjusted_fares)
