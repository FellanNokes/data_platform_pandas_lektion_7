import pandas as pd
import json


def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

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


products_jsonb = pd.read_csv("products_raw.csv")
print(products_jsonb)

products_jsonb["payload"] = products_jsonb["payload"].apply(json.loads)

payload_df = pd.json_normalize (products_jsonb ["payload"])
print(payload_df)

reject_condition = (
 (payload_df["name"] == "") |
 (payload_df["currency"] == "") |
 (payload_df["price"] <= 0) |
 (payload_df["quantity"] <= 0)
)

df_rejected = payload_df[reject_condition ].copy()
df_valid = payload_df[~reject_condition ].copy()

df_valid = clean_dataframe(df_valid)

print(df_valid)
print(df_rejected)
