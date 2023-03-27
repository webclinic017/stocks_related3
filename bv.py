import boto3

client = boto3.client('glue')

response = client.create_crawler(
    Name='SalesCSVCrawler',
    Role='AWSGlueServiceRoleDefault',
    DatabaseName='sales-cvs',
    Description='Crawler for generated Sales schema',
    Targets={
        'S3Targets': [
            {
                'Path': 's3://ejlp12-etl-demo-bucket/data/csv',
                'Exclusions': [
                ]
            },
        ]
    },
    SchemaChangePolicy={
        'UpdateBehavior': 'UPDATE_IN_DATABASE',
        'DeleteBehavior': 'DELETE_FROM_DATABASE'
    }
    #,Configuration='{ "Version": 1.0, "CrawlerOutput": { "Partitions": { "AddOrUpdateBehavior": "InheritFromTable" } } }'
)

response = client.start_crawler(
    Name='SalesCSVCrawler'
)

response = client.update_table(
    DatabaseName='sales-cvs',
    TableInput={
        'Name': 'csv',
        'Description': 'Table Sales',
        'StorageDescriptor': {
            'SerdeInfo': {
                'Name': 'OpenCSVSerde',
                'SerializationLibrary': 'org.apache.hadoop.hive.serde2.OpenCSVSerde',
                'Parameters': {
                    'separatorChar': ','
                }
            }
        }
    }
)
