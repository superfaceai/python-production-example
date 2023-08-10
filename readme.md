[Website](https://superface.ai) | [Get Started](https://superface.ai/docs/getting-started) | [Documentation](https://superface.ai/docs) | [GitHub Discussions](https://sfc.is/discussions) | [Twitter](https://twitter.com/superfaceai) | [Support](https://superface.ai/support)

<img src="https://github.com/superfaceai/one-sdk/raw/main/docs/LogoGreen.png" alt="Superface" width="100" height="100">

# Superface Comlink & OneSDK Production Example

This example demonstrates how to use Comlink files created using the [Superface CLI](https://github.com/superfaceai/cli) in a production setting with [OneSDK](https://github.com/superfaceai/one-sdk) and Python.

## Overview

The use case in this example is "sending an email". To do this, we are using the API of the email provider [Resend.com](https://resend.com).

The associated Comlink profile and Comlink map required by OneSDK for this use case were generated using the Superface CLI. You can see those files in the `superface` directory.

This example is a [Python](https://python.org) application using [Flask](https://flask.palletsprojects.com/) to create a server that will accept `POST` requests to an `/execute` endpoint, which will then invoke OneSDK to perform the use case tasks and send an email.

## Prerequisites

To work with this example you will need Python 3.8 or higher, as well as [PyPi](https://pypi.org).

To use [Resend](https://resend.com/) as the email API provider, you will need to register an account and create an API key. You must also verify the domain you want to send from, otherwise sending will be limited to the email address of the account holder only.

## Running the example

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/superfaceai/python-production-example.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your SUPERFACE_ONESDK_TOKEN and the RESEND_TOKEN for the Resend API:

```bash
SUPERFACE_ONESDK_TOKEN=
RESEND_TOKEN=
```

Run the server:

```bash
FLASK_APP=main flask run
```

This will run the development server using Nodemon on port 5000. The `/execute` endpoint is now available.

## Test the endpoint

With the server running, make a `POST` request using a tool or your choice such as [Postman](https://www.postman.com/), [HTTPie](https://httpie.io/) or [RapidAPI](https://paw.cloud/), to:

```bash
http://localhost:5000/execute
```

With the following JSON object as the body:

_HINT: Don't forget to replace the email addresses with real ones._

```json
{
  "to": "replace-with-your-email",
  "from": "replace-with-your-from-email",
  "subject": "Hello, World!",
  "text": "Hello, from Superface!"
}
```

For example, using cURL:

```bash
curl -X POST http://localhost:3000/execute -H 'Content-Type: application/json' -d '{ "to": "replace-with-your-email", "from": "replace-with-your-from-email", "subject": "Hello, World!", "text": "Hello, from Superface!"}'
```

On success you will see the `id` of the email sent returned from Resend.

If the request fails, you will get an error response from OneSDK.

## Deploying to production

If everything works locally, the next step would be to modify any aspects of `main.py` to your liking and deploy it to production.

### Example - Deploy to Fly.io

Fly.io is a service that can handle fast deploys hosted in regions of your choice. For example purposes, here's how to deploy this application with them.

Install the Fly.io tools

```bash
brew install flyctl
```

Launch a new machine:

```bash
fly launch
```

Then, add the content from your `.env` file to the ENV on the server:

```bash
fly secrets set SUPERFACE_ONESDK_TOKEN=yourtoken

fly secrets set RESEND_TOKEN=yourresendtoken
```

Then deploy the app to Fly.io

```bash
fly deploy
```

After a successful deployment you will be able to access the same `/execute` endpoint at:

```bash
https://<your-app-name>.fly.dev/execute
```

## License

OneSDK and this example application are licensed under the [MIT License](LICENSE).

© 2023 Superface s.r.o.
