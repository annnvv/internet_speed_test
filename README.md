# Internet Speed Testing

**Status**: In Progress

**Purpose**: To see whether my internet provider is providing a consistent internet speed.
In order to figure this out, I plan to query my internet speed periodically and store the data in a local PostgreSQL database.
Then, I plan to pull the data from the database and display it on a dashboard.


## Skills Utilized
- Define and create a PostgreSQL database table using `sqlalchemy`
- Create ETL script to :
    - Use `speedtest-cli` package to get internet download and upload speeds
    - Insert data into database table using `sqlalchemy`
    - Schedule the ETL script using `prefect` (maybe `cron`? tbd)
- create API interface to dashboard (using `fastAPI`)
- create a `streamlit` front-end dashboard    

TODO:
- change database to sqlite (no need for suped up postgresql. don't really need the jsonb column, it's a nice to have)
- change all column names to lower case in DB (it's just slightly annoying to have to escape those columns names)
- change all references to those columns in the various places
- think about changing from prefect to chron for orchestration (chron might get the job done easier here) 

## Lessons Learned




## Useful CLI commands

To launch the local prefect UI server:
```
prefect server start
```

To start the agent:
```
prefect agent start --work-queue "hourly_speed_test_queue"
```

To launch fastAPI development server:
```
uvicorn fastapi_routes:app --reload
```

To launch Streamlit server:
```
streamlit run streamlit_dashboard.py
```
