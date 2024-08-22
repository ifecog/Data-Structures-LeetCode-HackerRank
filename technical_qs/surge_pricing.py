def surge_pricing_adjustment(pricings):
    corrected_pricings = []
    
    for pricing in pricings:
        if pricing['location'] == 'city_center' and pricing['surge_multiplier'] < 1.5:
            pricing['surge_multiplier'] = 1.5
        
        if pricing['location'] == 'suburb' and pricing['surge_multiplier'] > 2.0:
            pricing['surge_multiplier'] = 2.0
            
        pricing['fare'] = round(pricing['surge_multiplier'] * pricing['base_fare'])
        
        corrected_pricings.append(pricing)
    
    return corrected_pricings


# Example usage

pricings = [
  {"id": "1", "location": "city_center", "base_fare": 20, "surge_multiplier": 1.2},
  {"id": "2", "location": "suburb", "base_fare": 15, "surge_multiplier": 2.5},
  {"id": "3", "location": "rural", "base_fare": 25, "surge_multiplier": 1.8}
]

adjusted_pricings = surge_pricing_adjustment(pricings)
print(adjusted_pricings)