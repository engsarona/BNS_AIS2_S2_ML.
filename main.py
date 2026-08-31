from config.config import DATA_PATH, COLS_TO_DROP
from preprocessing import (
    Read_data_file,
    Drop_unnecessary_features,
    Check_data_type
)


def main():
   
    print("--- 1. Reading Data ---")
    df = Read_data_file(DATA_PATH)

    if df is not None:

        print("\n--- 2. Data Quality Report (Before Dropping) ---")
        report_before = Check_data_type(df)
        print(report_before)

       
        print("\n--- 3. Dropping Unnecessary Features ---")
        df_cleaned = Drop_unnecessary_features(df, COLS_TO_DROP)

        
        print("\n--- 4. Data Quality Report (After Dropping) ---")
        report_after = Check_data_type(df_cleaned)
        print(report_after)


if __name__ == "__main__":
    main()