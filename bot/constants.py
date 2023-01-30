try:
    import authData
    TOKEN = authData.ACCESS_TOKEN
except ImportError:
    print("Missing authData.py module containing the `ACCESS_TOKEN` variable")
    exit(-1)
except AttributeError:
    print("Missing `ACCESS_TOKEN` variable in authData.py module")
    exit(-2)

# Configue constants
BASE_URL = "https://api.ciscospark.com/v1/"
HEADERS  = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}
