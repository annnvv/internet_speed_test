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
    - Schedule the ETL script using `prefect`
    
TODO:
- create API interface to dashboard (using `fastAPI`).

## Lessons Learned




## Useful CLI commands

To launch the local prefect UI server:
```
prefect orion start
```

To start the agent:
```
prefect agent start --work-queue "hourly_speed_test_queue"
```
