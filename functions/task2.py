#### Splitting Complex Tasks ######

## you are creating a monthly report for a cafe's sale.
## Instaed of putting all logic in one place, break it down into smaller functions.

### Write a function generate_report() that calls:
## - fetch sales
## - filter_valid_sales()
## - summarize_data()



def fetch_sales():
    print("Fetching sales data from the database...")


def filter_valid_sales():
    print("Filtering valid sales data...")

def summarize_data():
    print("Summarizing sales data...")


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Monthly sales report generated successfully!")


generate_report()
