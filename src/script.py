import requests
import tarfile
import os

url = "https://covid19.infn.it/iss/csv_part/iss.tar.gz"
response = requests.get(url, stream=True)
file = tarfile.open(fileobj=response.raw, mode="r|gz")
file.extractall(path=os.path.join(os.getcwd(),"0_archive\\"))


