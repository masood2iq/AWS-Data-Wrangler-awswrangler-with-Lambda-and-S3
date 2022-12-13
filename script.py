import json
import awswrangler as wr
from datetime import datetime

def lambda_handler(event, context):
    
    df = wr.s3.read_csv("s3://bucket-name/input/", dataset=True)
    
    df = df [["CUSTOMERNAME","EMAIL"]]
	
    wr.s3.to_json(df,"s3://bucket-name/output/mydata.json")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successful')
    }

