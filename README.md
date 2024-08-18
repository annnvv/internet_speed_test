# Internet Speed Testing

**Status**: In Progress

**Purpose**: To see whether my internet provider is providing a consistent internet speed.
In order to figure this out, I plan to query my internet speed periodically and store the data in a local database.
Then, I plan to pull the data from the database using API requests and display it on a dashboard.

## Workflow

1. Define SpeedTest class in **define_speed_test_class.py**
2. Create the sqlite db in **create_speed_test_db.py**
3. Create script to download and lightly transform the data in **get_speed_test_data.py**
4. Schedule the get_speed_test_data.py script to run hourly using cron 
5. Create api routes to query db in **fastapi_routes.py**
6. Create front-end visualization to display the data with download and upload speed reference levels in **streamlit_dashboard.py**


## Skills Utilized
- Define and create a ~PostgreSQL~ SQLite database table using `sqlalchemy`
- Create ETL script to :
    - Use `speedtest-cli` package to get internet download and upload speeds
    - Insert data into database table using `sqlalchemy`
    - Schedule the ETL script using `prefect` (maybe `cron`? tbd)
- create API interface to dashboard (using `fastAPI`)
- create a `Streamlit` front-end dashboard    

TODO:
- [DONE] change database to sqlite (no need for suped up postgresql. don't really need the jsonb column, it's a nice to have)
- [DONE] change all column names to lower case in DB (it's just slightly annoying to have to escape those columns names)
- [DONE] change all references to those columns in the various places
- think about changing from prefect to chron for orchestration (chron might get the job done easier here) 

## Lessons Learned
- refactoring the code from PostgreSQL to SQLite wasn't too challenging; it was just a matter of finding all of the relevant references and updating them
- Do NOT use capital letters in column names in a PostgreSQL database; you will need to escape them; just avoid it!


## Useful CLI commands

Cron commands

Every 150 Minutes	*/150 * * * * /path/to/scriptx
```
chmod +x script.python
crontab -e ##Create or Edit Crontab File
crontab -l ##Check Active Cron Jobs
```

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
