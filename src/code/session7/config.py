# config/config.py
#
# All dataset-specific settings live here.
# preprocessing.py should never hardcode column names / paths itself,
# it should just receive whatever this file (or the user) gives it.

# Path to the raw data file
DATA_FILE_PATH = "data/raw/titanic.csv"

# Columns that should be dropped because they don't add predictive value
# (IDs, free-text names, ticket numbers, etc.)
COLS_TO_DROP = ["PassengerId", "Name", "Ticket"]
