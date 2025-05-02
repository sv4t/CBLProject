import pandas as pd

def create_ward_crime_report(crime_df, lookup_df, median_home_prices_df):
    try:
        
        # Merge the dataframes on LSOA code
        merged_df = pd.merge(
            crime_df,
            lookup_df,
            on='LSOA code',
            how='left'
        )
        
        # Create a mapping of ward names to codes and local authorities
        ward_mapping = lookup_df.drop_duplicates(['Ward name', 'LAD24NM'])[['Ward name', 'WD24CD', 'LAD24NM']].set_index(['Ward name', 'LAD24NM'])
        
        # Group by both ward name and local authority to handle same-named wards in different authorities
        ward_stats = merged_df.groupby(['Ward name', 'LAD24NM']).size().sort_values(ascending=False)
        
        # Calculate percentages
        total_crimes = ward_stats.sum()
        
        # Get median home prices for April 2023
        target_date = merged_df['Month'].iloc[0]
        date_columns = median_home_prices_df.columns[4:]
        closest_date = min(date_columns, key=lambda x: abs(pd.to_datetime(x) - pd.to_datetime(target_date)))
        
        # Create a mapping of ward name and local authority to median home price
        price_mapping = median_home_prices_df.set_index(['Ward name', 'Local authority name'])[closest_date]
        
        # Create a function to look up prices using both ward name and local authority
        def get_ward_price(ward_info):
            ward_name, local_authority = ward_info
            try:
                price = price_mapping.get((ward_name, local_authority))
                return price
            except:
                return None
        
        # Create the final DataFrame
        ward_stats_df = pd.DataFrame({
            'Ward Name': ward_stats.index.get_level_values('Ward name'),
            'Local Authority': ward_stats.index.get_level_values('LAD24NM'),
            'Ward Code': ward_stats.index.map(lambda x: ward_mapping.loc[x, 'WD24CD']),
            'Total Crimes': ward_stats.values,
            'Percentage of All Crimes': (ward_stats / total_crimes * 100).round(4),
            'Median Home Price': ward_stats.index.map(get_ward_price)
        })
        
        # Save statistics to a new CSV file
        output_path = 'C:/Users/alexz/OneDrive - TU Eindhoven/CBLProject/ward_crime_statistics.csv'
        ward_stats_df.to_csv(output_path, index=False)
        print(f"Ward crime statistics have been saved to: {output_path}")

        
    except FileNotFoundError as e:
        print(f"Error: Could not find one of the required files: {e}")
    except pd.errors.EmptyDataError:
        print("Error: One of the data files is empty")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



def create_burglary_ward_crime_report(burglary_df, lookup_df, median_home_prices_df):
    try:
        # Merge the dataframes on LSOA code
        merged_df = pd.merge(
            burglary_df,
            lookup_df,
            on='LSOA code',
            how='left'
        )
        
        # Create a mapping of ward names to codes and local authorities
        ward_mapping = lookup_df.drop_duplicates(['Ward name', 'LAD24NM'])[['Ward name', 'WD24CD', 'LAD24NM']].set_index(['Ward name', 'LAD24NM'])
        
        # Group by both ward name and local authority to handle same-named wards in different authorities
        ward_stats = merged_df.groupby(['Ward name', 'LAD24NM']).size().sort_values(ascending=False)
        
        # Calculate percentages
        total_crimes = ward_stats.sum()
        
        # Get median home prices for April 2023
        target_date = merged_df['Month'].iloc[0]
        date_columns = median_home_prices_df.columns[4:]
        closest_date = min(date_columns, key=lambda x: abs(pd.to_datetime(x) - pd.to_datetime(target_date)))
        
        # Create a mapping of ward name and local authority to median home price
        price_mapping = median_home_prices_df.set_index(['Ward name', 'Local authority name'])[closest_date]
        
        # Create a function to look up prices using both ward name and local authority
        def get_ward_price(ward_info):
            ward_name, local_authority = ward_info
            try:
                price = price_mapping.get((ward_name, local_authority))
                return price
            except:
                return None


        # Create the final DataFrame
        ward_stats_df = pd.DataFrame({
            'Ward Name': ward_stats.index.get_level_values('Ward name'),
            'Local Authority': ward_stats.index.get_level_values('LAD24NM'),
            'Ward Code': ward_stats.index.map(lambda x: ward_mapping.loc[x, 'WD24CD']),
            'Total Burglaries': ward_stats.values,
            'Percentage of All Burglaries': (ward_stats / total_crimes * 100).round(4),
            'Median Home Price': ward_stats.index.map(get_ward_price)
        })
        
        # Save statistics to a new CSV file
        output_path = 'C:/Users/alexz/OneDrive - TU Eindhoven/CBLProject/ward_burglary_statistics.csv'
        ward_stats_df.to_csv(output_path, index=False)
        print(f"Ward burglary statistics have been saved to: {output_path}")

    except FileNotFoundError as e:
        print(f"Error: Could not find one of the required files: {e}")
    except pd.errors.EmptyDataError:
        print("Error: One of the data files is empty")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":

    # Load the crime database
    # Put your path here
    crime_df = pd.read_csv('C:/Users/alexz/OneDrive - TU Eindhoven/CBLProject/CrimeData/2022-04/2022-04-metropolitan-street.csv')

    # Filter for burglaries only
    # Put your path here
    burglary_df = crime_df[crime_df['Crime type'] == 'Burglary']

    # Load the LSOA to Ward lookup database
    # Put your path here
    lookup_df = pd.read_csv('C:/Users/alexz/OneDrive - TU Eindhoven/CBLProject/LSOA_to_Electoral_Ward.csv')

    # Load the median home prices by ward database
    median_home_prices_df = pd.read_csv('C:/Users/alexz/OneDrive - TU Eindhoven/CBLProject/MedianHomePriceByWard.csv')


    create_ward_crime_report(crime_df, lookup_df, median_home_prices_df)
    create_burglary_ward_crime_report(burglary_df, lookup_df, median_home_prices_df)
