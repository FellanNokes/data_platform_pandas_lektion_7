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
    print(product_df["price"].sort_values())# Sorting algorithm == ?? # TODO - Research

    print(product_df.describe())            # Statistics of Numerical data