def snowflake_json_ingestion():

    import snowflake as sf
    
    sfAccount = input("Enter Account Name: ")#"claritypartner.east-us-2.azure"
    sfUser    = input("Enter Username: ") #"dkochar"
    
    sfPswd = ""
    
    # Request user password if not provided already
    if sfPswd == "":
        import getpass
        sfPswd = getpass.getpass("Enter Password: ")
        
    # Test the connection to Snowflake by retrieving the version number
    from sqlalchemy import create_engine
    engine = create_engine("snowflake://{user}:{password}@{account}/".format(
        user     = sfUser,
        password = sfPswd,
        account  = sfAccount,
      )
    )
    try:
        connection = engine.connect()
        print("Connection successful!")
        connection.close()
    except:
        print("Connection failed. Please check credentials")
    finally:
        engine.dispose()

    sfDatabase   = input("Enter Database Name: ")
    sfSchema     = input("Enter Schema Name: ")
    sfWarehouse  = input("Enter Warehouse Name: ")
    jsonURL      = input("Enter JSON URL: ")
    sfStage      = input("Enter Stage Name: ")
    sfStageTable = input("Enter Staging Table Name: ")
    
    import urllib, json
    
    jsonRaw = json.loads(urllib.request.urlopen(jsonURL).read())
    
    fname = jsonURL.rsplit('/', 1)[-1]
    
    with open(fname, "w") as outfile:
        json.dump(jsonRaw, outfile)
    
    # Open connection to Snowflake
    con = sf.connector.connect(
      user = sfUser,
      password = sfPswd,
      account = sfAccount,
    )
    
    sfq = con.cursor()
    
    # Set file path
    import os
    pwd       = os.getcwd()
    file_path = f"file://{pwd}\{fname}"
    
    # Set Snowflake context
    sfq.execute(f"USE WAREHOUSE {sfWarehouse}")
    sfq.execute(f"USE DATABASE {sfDatabase}")
    sfq.execute(f"USE SCHEMA {sfSchema}")
    
    # Create or replace JSON file format for loading stage
    sfq.execute("CREATE OR REPLACE FILE FORMAT JSON_FILE_FORMAT TYPE = 'JSON' "\
    "COMPRESSION = 'AUTO' "\
    "ENABLE_OCTAL = FALSE "\
    "ALLOW_DUPLICATE = FALSE "\
    "STRIP_OUTER_ARRAY = TRUE "\
    "STRIP_NULL_VALUES = FALSE "\
    "IGNORE_UTF8_ERRORS = FALSE")
    
    # Stage json locally dumped file
    sfq.execute(f"PUT {file_path} @%{sfStage} auto_compress=TRUE")
    
    # Load staging table
    sfq.execute(f"COPY INTO {sfStageTable} from @%{sfStage}/{fname}.gz file_format = JSON_FILE_FORMAT")
    
    print(f"Successfuly loaded json from {jsonURL} into {sfStageTable}")
        
if __name__ == '__main__':
    snowflake_json_ingestion()