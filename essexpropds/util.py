import pyodbc
import pandas as pd
def sql_conn(database, query, server="essexbi"):
    '''
    Usage: Read data from a sql server as a pandas dataframe by establishing a trusted pyodbc connection
    Parameters: - str Database: name of the database for the table specified in the query
                - str Query: The full SQL query for the data encased in triple double-quotations (ex: """ SELECT * 
                                                                                                        FROM table """)
                - str Server: name of the server for the database specified; by default essexbi
    Return:     - pd.Dataframe queryDf: the queried data 
    '''

    
    sqlconn = pyodbc.connect(
        driver='SQL Server',
        host=server,
        database=database,
        Trusted_Connection="yes",
    )
    
    with sqlconn:
        df_query = pd.read_sql(query, sqlconn)
    print(df_query.shape)
    print(df_query.columns)
    return df_query