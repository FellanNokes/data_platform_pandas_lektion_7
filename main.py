import pandas as pd

if __name__ == '__main__':

    # Dataframe (table)
    product_df = pd.DataFrame(
        {
            "id": ["SKU-1","SKU-2","SKU-3","SKU-4","SKU-5"],
            "name": ["Shoes", "Pants", "Shirts", "Sweaters", "Jackets"],
            "price": [299, 520, 600, 550, 5400],
            "currency": ["SEK", "SEK", "SEK", "SEK", "SEK"], # TODO - Missing values for CSV files when loaded (Crash)
        }
    )

    print(product_df) # Might take some time (first run)

    # Helper Methods / Utility Methods (pandas)
    print(product_df["price"].max())        # Highest Value
    print(product_df["price"].min())        # Minimum Value
    print(product_df["price"].mean())       # Mean of Total
    print(product_df["price"].median())     # Median of Total


    print(product_df.describe())            # Statistics of Numerical data

    print(product_df.sort_values("price"))  # Sorting algorithm == ?? # TODO - Research

    # to_* (exporting files)
    product_df.to_csv("products.csv", index=False) # Path = project folder

    #########################################################
    ################# DIRTY DATA FRAMES #####################
    #########################################################

    dirty_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", "SKU-3", "sku_4", "SKU5"],
            "name": [" Shoes", "pants", "SHIRTS", " SweaTers ", "designer  jackets"],
            "price": [" 299 ", "520", "600", "550 ", " 5400"],
            "currency": [" sek", "SEK", "SeK", "sek ", "SEK"],  # TODO - Missing values for CSV files when loaded (Crash)
        }
    )

    ## dirty_df.id = [cleaned strings] <--- FALSE
    # dirty_df["id"].strip() # This won't properly replace values in Series (columns)
    dirty_df["id"] = dirty_df["id"].str.strip() # Remove Whitespaces (start/end of string)
    dirty_df["id"] = dirty_df["id"].str.upper() # ALL CAPS
    dirty_df["id"] = dirty_df["id"].str.replace(" ", "").str.replace("_", "-") # Replace string content

    ## EDGE CASES ##
    # SKU5 <-- which EXCLUDES '-', Danger zone, because transformation isn't adding symbols...
    # SKU_4 <-- Technical Danger zone, what if multiple -- exists?

    dirty_df["price"] = dirty_df["price"].astype(float) # Casts: Current-Datatype -> float

    dirty_df["name"] = dirty_df["name"].str.strip()
    dirty_df["name"] = dirty_df["name"].str.title()
    dirty_df["name"] = dirty_df["name"].str.replace(r"\s+", " ", regex = True) # regex, value, bool

    dirty_df["currency"] = dirty_df["currency"].str.strip().str.upper()

    print(dirty_df.values)

    #########################################################
    ################# MISSING DATA FRAMES ###################
    #########################################################

    missing_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", None, "sku_4", "SKU5 "],
            "name": [" Shoes", None, "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", None, "550 ", " 4500"],
            "currency": [" sek", "SEK ", "Sek", None, " SEK"],
        }
    )

    print(missing_df.isna()) # Pandas tool for identifying TRUE missing values

    # TODO - helper method for quick assigning multiple columns
    # Flag missing values, helps decide strategy later on
    missing_df["id_missing"] = missing_df["id"].isna()
    missing_df["name_missing"] = missing_df["name"].isna()
    missing_df["price_missing"] = missing_df["price"].isna()
    missing_df["currency_missing"] = missing_df["currency"].isna()

    print(missing_df)