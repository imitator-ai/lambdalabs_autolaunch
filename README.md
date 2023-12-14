Setup:
1. `pip install -r requirements.txt`
2. `cp .env.example .env`
3. `vim .env` and set your configuration details
   - instance type identifiers are:
```
gpu_8x_h100_sxm5
gpu_1x_h100_pcie
gpu_8x_a100_80gb_sxm4
gpu_1x_a10
gpu_1x_rtx6000
gpu_1x_a100
gpu_1x_a100_sxm4
gpu_2x_a100
gpu_4x_a100
gpu_8x_a100
gpu_1x_a6000
gpu_2x_a6000
gpu_4x_a6000
gpu_8x_v100
```
  
Usage:
- `python main.py` will start polling for availability of the configured instance types until the instance is avaialble.
- Once the script detects that configured instance type is available, it will attempt to launch it and will send the notification to the webhook.
- After attempting to launch one instance, script exits.
