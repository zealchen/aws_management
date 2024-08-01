import boto3

# 创建 Lightsail 客户端
client = boto3.client('lightsail')

# 获取实例列表
response = client.get_instances()

# 打印实例列表
instances = response['instances']
for instance in instances:
    print(f"Name: {instance['name']}")
    print(f"State: {instance['state']['name']}")
    print(f"Created At: {instance['createdAt']}")
    print(f"Blueprint Id: {instance['blueprintId']}")
    print(f"Bundle Id: {instance['bundleId']}")
    print('-' * 60)
