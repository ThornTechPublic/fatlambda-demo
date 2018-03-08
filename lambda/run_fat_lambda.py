import boto3


def lambda_handler(event, context):
    response = boto3.client(service_name='ecs').run_task(
        cluster='<enter cluster name>',
        taskDefinition='<enter task definition name>',
        launchType='FARGATE',
        networkConfiguration={
            'awsvpcConfiguration': {
                'subnets': [
                    '<enter subnet 1>',
                    '<enter subnet 2>'
                ],
                'securityGroups': [
                    '<enter security group>',
                ],
                'assignPublicIp': 'DISABLED'
            }
        }
    )
    return 'ecs run task response: %s' % response
