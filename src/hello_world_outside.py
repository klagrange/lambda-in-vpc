import json
import os
import requests

def main(_event, _context):
    ALB = os.environ["ALB"]
    res = requests.get(ALB)

    display = {
        "message": "Hello World from **CUSTOM** VPC",
        "ALB": ALB,
        "alb_res": res.status_code
    }

    return {
        "statusCode": 200,
        "body": json.dumps(display)
    }

if __name__ == "__main__":
    res = main('', '')
    print(res)