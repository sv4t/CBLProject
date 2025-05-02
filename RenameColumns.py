import pandas as pd

def rename_year_ending_columns(input_file, output_file):
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Dictionary to convert month names to numbers
        month_to_num = {
            'Jan': '01', 'Feb': '02', 'Mar': '03', 'Apr': '04',
            'May': '05', 'Jun': '06', 'Jul': '07', 'Aug': '08',
            'Sep': '09', 'Oct': '10', 'Nov': '11', 'Dec': '12'
        }
        
        # Function to transform column name
        def transform_column_name(col_name):
            if not isinstance(col_name, str) or not col_name.startswith('Year ending'):
                return col_name
                
            parts = col_name.split()
            if len(parts) >= 4 and parts[0] == 'Year' and parts[1] == 'ending':
                month = parts[2][:3]  # Get first 3 letters of month
                year = parts[3]
                if month in month_to_num:
                    return f"{year}-{month_to_num[month]}"
            return col_name

        # Create a dictionary of old column names to new column names
        column_mapping = {col: transform_column_name(col) for col in df.columns}
        
        # Rename the columns
        df = df.rename(columns=column_mapping)
        
        # Save the modified DataFrame to a new CSV file
        df.to_csv(output_file, index=False)
        print(f"Columns renamed successfully. New file saved as: {output_file}")
        
        # Print the mapping for verification
        print("\nColumn name changes:")
        for old, new in column_mapping.items():
            if old != new:
                print(f"'{old}' -> '{new}'")
                
    except FileNotFoundError:
        print(f"Error: Could not find the input file: {input_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # File paths
    input_csv = "C:/Users/alexz/OneDrive - TU Eindhoven/CBLProject/MedianHomePriceByWard.csv"  # Replace with your input file path
    output_csv = "C:/Users/alexz/OneDrive - TU Eindhoven/CBLProject/MedianHomePriceByWard_ReformattedDates.csv"
    
    rename_year_ending_columns(input_csv, output_csv)
