from shroomdk import ShroomDK
import pandas as pd

# Initialize `ShroomDK` with your API Key
sdk = ShroomDK("e7043161-2bb0-4bc7-b5d4-c7aa7985b349")

Df = pd.Dataframe()
# Parameters can be passed into SQL statements 
# via native string interpolation
#my_address = "0xf2ff2bc69fb16674d0cc58bcdd7f674db576bc77"
sql = f"""
    SELECT
        date_trunc('day', block_timestamp) AS day,
        tx_json:receipt:logs,
        tx_hash
    FROM
        optimism.core.fact_transactions
    WHERE
        CONTAINS(tx_json:receipt:logs:: string, '0x4200000000000000000000000000000000000042')
    AND day>='2022-09-01'
"""

# Run the query against Flipside's query engine 
# and await the results
query_result_set = sdk.query(sql)

for record in query_result_set.records:
    Df['Day'] = record['day']
    Df['JSON'] = record['tx_json:receipt:logs']
    Df['Tx'] = record['tx']
    print(f"{Df['JSON']} \n")

started_at = query_result_set.run_stats.started_at
ended_at = query_result_set.run_stats.ended_at
elapsed_seconds = query_result_set.run_stats.elapsed_seconds
record_count = query_result_set.run_stats.record_count

print(f"This query took ${elapsed_seconds} seconds to run and returned {record_count} records from the database.")