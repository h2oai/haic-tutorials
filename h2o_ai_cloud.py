import h2o_authn 
import getpass 

import h2o_mlops
import h2o_engine_manager

# The URL you use to access the H2O AI Cloud's UI - do not include the `https://` - ex: internal.dedicated.h2o.ai
H2O_CLOUD_URL = "internal.dedicated.h2o.ai"


# Information available at https://H2O_CLOUD_URL/cli-and-api-access
TOKEN_ENDPOINT = "https://auth.internal.dedicated.h2o.ai/auth/realms/hac/protocol/openid-connect/token"
API_CLIENT_ID = "hac-platform-public"
REFRESH_TOKEN_URL = "https://internal.dedicated.h2o.ai/auth/get-platform-token"


def token_provider():
    """
    Connect to the H2O AI Cloud
    If these notebooks are running within a HAIC environment, the os variables will exist automatically as App Secrets.
    When running these notebooks locally, you can update these variables based on the values in the CLI & API Acess page by
        clicking on your name from the H2O AI Cloud UI.
    """
    
    print(f"Visit {REFRESH_TOKEN_URL} to get your platform token")

    return h2o_authn.TokenProvider(
        refresh_token=getpass.getpass('Enter your platform token: '),
        client_id=API_CLIENT_ID,
        token_endpoint_url=TOKEN_ENDPOINT
    )


def mlops_client():
    """
    Connect to MLOps
    """
    return h2o_mlops.Client(
        h2o_cloud_url="https://" + H2O_CLOUD_URL,
        token_provider=token_provider()
    )


def ai_engine_client():
    """
    Connect to Notebooks, Driverless AI, and H2O-3 AI Engines
    """
    return h2o_engine_manager.login(
        environment="https://" + H2O_CLOUD_URL,
        token_provider=token_provider()
    )