import yaml
from fastapi import FastAPI
import asyncpg

app = FastAPI()

# Function to establish a database connection
async def get_database_connection():

    with open("database/config.yaml", "r") as f:
        config = yaml.safe_load(f)
    
    return await asyncpg.connect(
        user=config['db']['user_name'],
        password=config['db']['password'],
        database=config['db']['db_name'],
        host=config['db']['host_name'],
    )


@app.get("/get_avg_download_speed/")
async def execute_get_avg_download_speed():
    query = "SELECT AVG(\"download_speed_Mb\") AS average_download_speed FROM speed_test;"

    try:
        conn = await get_database_connection()

        result = await conn.fetch(query)

        return {"average_download_speed": result[0]['average_download_speed']}  # Return the average download speed
    except Exception as e:
        return {"error": str(e)}
    finally:
        await conn.close() 


@app.get("/get_avg_download_speed_by_day/")
async def execute_get_avg_download_speed_by_day():
    query = "SELECT AVG(\"download_speed_Mb\") AS average_download_speed, TO_CHAR(timestamp:: DATE, \'mm-dd-yyyy') as date FROM speed_test GROUP BY date;"

    try:
        conn = await get_database_connection()

        result = await conn.fetch(query)

        # Prepare the result as a dictionary ##av.note: sure I want to keep this as a dictionary
        formatted_result = [{"date": row['date'], "average_download_speed": row['average_download_speed']}
                            for row in result]

        return {"average_by_day": formatted_result} 
    
    except Exception as e:
        return {"error": str(e)}
    finally:
        await conn.close()


@app.get("/get_data_all/")
async def execute_get_data_all():
    query = "SELECT * FROM speed_test;"

    try:
        conn = await get_database_connection()
        result = await conn.fetch(query)
        return result
    except Exception as e:
        return {"error": str(e)}
    finally:
        await conn.close()