from maclookup import ApiClient
api_key = input("Enter API key : ")
#api_key = os.environ['API_KEY']
client = ApiClient(api_key)
mac_adress=input("Enter the mac address : ")
response = client.get(mac_adress)
output=response.vendor_details.company_name
print("Company Name: ",output)


