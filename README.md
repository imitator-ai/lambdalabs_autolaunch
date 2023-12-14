Setup:
1. `pip install -r requirements.txt`
2. `cp .env.example .env`
3. `vim .env` and set your configuration details
   - instance type identifiers are available at https://cloud.lambdalabs.com/api/v1/instance-types
  
Usage:
- `python main.py` will start polling for availability of the configured instance types until the instance is avaialble.
- Once the script detects that configured instance type is available, it will attempt to launch it and will send the notification to the webhook.
- After attempting to launch, script exits.
