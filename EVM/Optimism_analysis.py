from shroomdk import ShroomDK
import pandas as pd
import datetime

# Initialize `ShroomDK` with your API Key
sdk = ShroomDK("e7043161-2bb0-4bc7-b5d4-c7aa7985b349")

Start = datetime.datetime.today()
Day = Start

Df = pd.DataFrame()
# Parameters can be passed into SQL statements 
# via native string interpolation
while Day >= datetime.datetime(2022,9,1):
    Daylastweek = Day - datetime.timedelta(hours = 12)
    #print(Daylastweek)
    D  = f"{Day.year}-{Day.month}-{Day.day} {Day.hour}"
    #print(D)
    D_7 = f"{Daylastweek.year}-{Daylastweek.month}-{Daylastweek.day} {Daylastweek.hour}"
    #print(D_7)
    print(f"The querry is before {Day}")
    print(f"The querry is after {Daylastweek}")
    sql = f"""
        SELECT
            *,
            date_trunc('hour', block_timestamp) as day
        FROM
            optimism.core.fact_event_logs
        WHERE
            contract_address = '0x4200000000000000000000000000000000000042'
        AND (day > '{D_7}' AND day <= '{D}')
            """

    # Run the query against Flipside's query engine 
    # and await the results
    query_result_set = sdk.query(sql)

    Df = Df.append(query_result_set.records)
    """ for record in query_result_set.records:
        print(record)
        Df = Df.append(record, ignore_index = True) """
    print(f"{Df} \n")
    Day = Daylastweek

    started_at = query_result_set.run_stats.started_at
    ended_at = query_result_set.run_stats.ended_at
    elapsed_seconds = query_result_set.run_stats.elapsed_seconds
    record_count = query_result_set.run_stats.record_count

    print(f"This query took ${elapsed_seconds} seconds to run and returned {record_count} records from the database.")
Df.to_pickle(f"C:/Users/vlist/.vscode/GitHub/Data-analysis/EVMExport_Df.pkl")