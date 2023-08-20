select customer_id, email, gender, city, country
from {{ source("raw_data", "customers") }}
