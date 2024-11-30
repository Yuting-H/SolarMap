# importing geopy library and Nominatim class
import pgeocode

country_code = input("Enter a 2-letter country code (e.g., 'us' for United States, 'ca' for Canada): ").strip().lower()
zip_code = input("Enter a ZIP Code: ").strip()

if country_code and zip_code:
    try:
        # calling the Nominatim tool and create Nominatim class
        loc = pgeocode.Nominatim(country_code)
        location_info = loc.query_postal_code(zip_code)

        # check for valid longitude and latitude
        if not location_info[['latitude', 'longitude']].isna().any():
            print(f"ZIP code: {zip_code}")
            print(f"Latitude: {location_info['latitude']}, Longitude: {location_info['longitude']}")
        else:
            print(f"Postal code {zip_code} is invalid or not found in the {country_code.upper()} dataset.")
    except ValueError as e:
        print(f"Error: {e}. Please ensure the country code is valid.")
else:
    print("No ZIP code entered.")

