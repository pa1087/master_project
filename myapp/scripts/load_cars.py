import csv
from myapp.models import Car

def load_csv_data(file_path):
    # Open the CSV file
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Iterate over each row in the CSV
        for row in reader:
            # Create a Car object for each row and save it to the database
            Car.objects.create(
                price=float(row['price']),          # Convert price to a float
                brand=row['brand'],                 # Directly map brand
                model=row['model'],                 # Directly map model
                year=int(row['year']),              # Convert year to integer
                title_status=row['title_status'],   # Directly map title_status
                mileage=float(row['mileage']),      # Convert mileage to float
                color=row['color'],                 # Directly map color
                vin=row['vin'],                     # Directly map vin
                lot=row['lot'],                     # Directly map lot
                state=row['state'],                 # Directly map state
                country=row['country'],             # Directly map country
                condition=row['condition']          # Directly map condition
            )
    print("Cars data loaded successfully.")

