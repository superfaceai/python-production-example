from flask import Flask, request
import os
from dotenv import load_dotenv
import sys
from one_sdk import OneClient, PerformError, UnexpectedError

load_dotenv()

app = Flask(__name__)


@app.route("/execute", methods=['POST'])
def execute_use_case():

    client = OneClient(
        # The token for monitoring your Comlinks at https://superface.ai
        token=os.getenv("SUPERFACE_ONESDK_TOKEN"),
        # Path to Comlinks within your project
        assets_path="./superface"
    )

    comlinkProfile = client.get_profile("email-communication/email-sending")
    use_case = comlinkProfile.get_usecase("SendEmail")

    inputs = request.get_json()

    try:
        r = use_case.perform(
            inputs,
            provider="resend",
            parameters={},
            security={"bearerAuth": {"token": os.getenv('RESEND_TOKEN')}}
        )

        print(f"RESULT: {r}")
        return r

    except Exception as e:
        if isinstance(e, PerformError):
            print(f"ERROR RESULT: {e.error_result}")
            return (e.error_result, e.error_result["error"]["code"])
        elif isinstance(e, UnexpectedError):
            print(f"ERROR:", e, file=sys.stderr)
            return ({"error": "There was an unexpected error."}, 500)
        else:
            raise e
    finally:
        client.send_metrics_to_superface()
