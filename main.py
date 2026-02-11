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

    def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()

        # --- ID: normalize to pattern like "SKU-5"
        df["id"] = df["id"].astype("string")

        df["id"] = (
            df["id"]
            .str.strip()
            .str.upper()
            .str.replace(r"\s+", "", regex=True)  # remove all whitespace anywhere
            .str.replace("_", "-", regex=False)  # underscores -> hyphens
            .str.replace(r"-+", "-", regex=True)  # collapse multiple hyphens
        )

        # Add hyphen if someone wrote "SKU5" instead of "SKU-5"
        df["id"] = df["id"].str.replace(r"^SKU(\d+)$", r"SKU-\1", regex=True)

        # Optional: force IDs to match SKU-<digits>; non-matching -> <NA>
        # df["id"] = df["id"].where(df["id"].str.match(r"^SKU-\d+$", na=False), pd.NA)

        # --- PRICE: safe numeric conversion
        df["price"] = pd.to_numeric(df["price"].astype("string").str.strip(), errors="coerce")

        # --- NAME: normalize whitespace + title case
        df["name"] = (
            df["name"]
            .astype("string")
            .str.strip()
            .str.replace(r"\s+", " ", regex=True)
            .str.title()
        )

        # --- CURRENCY: strip + uppercase, keep missing as <NA>
        df["currency"] = (
            df["currency"]
            .astype("string")
            .str.strip()
            .str.upper()
        )

        return df
        
    dirty_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", "SKU-3", "sku_4", "SKU5"],
            "name": [" Shoes", "pants", "SHIRTS", " SweaTers ", "designer  jackets"],
            "price": [" 299 ", "520.59", "600", "550 ", " 5400"],
            "currency": [" sek", "SEK", "SeK", "sek ", "SEK"],  # TODO - Missing values for CSV files when loaded (Crash)
        }
    )

    cleaned_df = clean_dataframe(dirty_df)

    

    print(cleaned_df.values)

    #########################################################
    ################# MISSING DATA FRAMES ###################
    #########################################################

    def flag_dataframe(df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        df["status"] = ""

        if df["id"].isna().any():
            df.loc[df["id"].isna(), "status"] += "Missing ID; "
        if df["name"].isna().any():
            df.loc[df["name"].isna(), "status"] += "Missing Name; "
        if df["price"].isna().any():
            df.loc[df["price"].isna(), "status"] += "Missing Price; "
        if df["currency"].isna().any():
            df.loc[df["currency"].isna(), "status"] += "Missing Currency; "

        df.loc[df["status"] == "", "status"] = "ACCEPTED"
        return df

    missing_df = pd.DataFrame(
        {
            "id": [" sku-1 ", "SKU- 2", None, "sku_4", "SKU5 "],
            "name": [" Shoes", None, "SHIRTS", " SweaTers ", "designer  jacket"],
            "price": [" 760 ", "520", None, "550 ", " 4500"],
            "currency": [" sek", "SEK ", None, None, " SEK"],
        }
    )

    print(missing_df.isna()) # Pandas tool for identifying TRUE missing values

    cleaned_df2 = clean_dataframe(missing_df)
    flagged_df = flag_dataframe(cleaned_df2)

    print(flagged_df)
    print(cleaned_df2)