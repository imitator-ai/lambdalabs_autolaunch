import requests
import json
import os


def send_to_slack(msg):
    url = os.getenv('SLACK_WEBHOOK_URL')
    payload = json.dumps({
        "text": msg
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return response.text


def launch_instance(instance_type_name, ssh_key, region):
    url = "https://cloud.lambdalabs.com/api/v1/instance-operations/launch"
    payload = json.dumps({
        "region_name": region,
        "instance_type_name": instance_type_name,
        "ssh_key_names": [
            ssh_key
        ],
        "file_system_names": [],
        "quantity": 1,
        "name": f"{ssh_key}/"
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + os.getenv('LAMBDALABS_API_KEY')
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()

    return response


def get_available_instances():
    url = "https://cloud.lambdalabs.com/api/v1/instance-types"
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic ' + os.getenv('LAMBDALABS_API_KEY')
    }

    response = requests.request("GET", url, headers=headers).json()

    return response


if __name__ == '__main__':
    import time
    from dotenv import load_dotenv

    load_dotenv()

    instance_type = os.getenv('INSTANCE_TYPE')
    ssh_key = os.getenv('SSH_KEY')

    while True:
        instances_availability = get_available_instances()
        avail_regions = instances_availability['data'][instance_type]['regions_with_capacity_available']
        print(f"{instance_type} regions: {avail_regions}")

        if len(avail_regions) > 0:
            send_to_slack(f"Launching {instance_type} in: {avail_regions[0]}")
            launch_result = launch_instance(instance_type, ssh_key, avail_regions[0]['name'])
            if 'error' in launch_result:
                send_to_slack(f"Error launching {instance_type} in {avail_regions[0]}: {launch_result['error']['message']}")
            else:
                send_to_slack(f"Launched {instance_type} in {avail_regions[0]}.")
                break

        time.sleep(10)
