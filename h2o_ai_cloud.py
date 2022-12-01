import getpass

import h2o_authn
import h2o_mlops_client
import h2osteam


# The URL you use to access the H2O AI Cloud's UI - do not include the `https://` - ex: cloud.h2o.ai
H2O_CLOUD_URL = "cloud-dev.h2o.ai"


# Information available at https://H2O_CLOUD_URL/cli-and-api-access
TOKEN_ENDPOINT = "https://auth.cloud-dev.h2o.ai/auth/realms/hac-dev/protocol/openid-connect/token"
API_CLIENT_ID = "hac-platform-public"
REFRESH_TOKEN_URL = "https://cloud-dev.h2o.ai/auth/get-platform-token"


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
    MLOPS_API = "https://mlops-api." + H2O_CLOUD_URL
    
    return h2o_mlops_client.Client(
        gateway_url=MLOPS_API,
        token_provider=token_provider()
    )



def steam_client():
    """
    Connect to Enterprise Steam, Driverless AI, and H2O-3
    """
    tp = token_provider()
    STEAM_API = "https://steam." + H2O_CLOUD_URL
    
    return h2osteam.login(
        url=STEAM_API,
        access_token=tp()
    )


