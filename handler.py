import json
import os
from mysql.connector import connect
from mysql import connector


def GetConnection():
    conn = None
    conn = connector.connect(
        host=os.environ.get("TLOG_DB_HOST"),
        user=os.environ.get("TLOG_DB_USER"),
        passwd=os.environ.get("TLOG_DB_PASS"),
        port=3306,
        db="tlog_dashboard_db",
    )
    return conn


def CacheCleanup(Date):
    proc = ""
    result = []

    proc = "tlog_dashboard_db."
    args = Date

    result = executeGet(proc, args, cursor)
    return result


def executeGet(proc, args, cursor):
    try:
        result = []
        cursor.callproc(proc, args)
        for result in cursor.stored_results():
            dataset = result.fetchall()
            columns = result.description
        result = []
        for value in dataset:
            tmp = {}
            for index, column in enumerate(value):
                tmp[columns[index][0]] = column
            result.append(tmp)

    except connector.Error as e:
        result = e

    return result


def main(event, context):
    conn = GetConnection()
    cursor = conn.cursor()
    Result = []
    GrossSales = []
    HourlySales = []

    StatusMessage = CacheCleanup(Date)

    Result.append({"StatusMessage": StatusMessage})

    conn.close()

    # TODO implement
    return {"StatusCode": 200, "Result": Result}
