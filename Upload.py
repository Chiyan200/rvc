import json
import requests
import zipfile
import os

def create_zip(folder_path, zip_name):
    """
    Create a zip file from the contents of a folder.

    :param folder_path: Path to the folder to be zipped.
    :param zip_name: Name of the resulting zip file.
    """
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))

folder_to_zip = r"F:\voiceModel\finalChareactersVoices\miniLog"
zip_file_name = 'miniLog.zip'
create_zip(folder_to_zip, zip_file_name)



header ={
    'authorization':"Bearer ya29.a0AXooCgtxgxSywJHCLohy_UL3bszM9zEJRMLvwYwkkGPqsZuirADYNGWm15jdYh1TtucW92pojf_GbTiK6vbPdBG4w7ga4UtMZpRGUhHyFFVhxVRYdEWcFT3ruWZ73yiPwi7iAU8kQFcVBzY82W7uNP4E6d3fKJl6BpPXaCgYKAUUSARASFQHGX2MiSmWNE5Djyb7ozcf2NPyZsg0171"
}
param={
    "name":"Applio-3.1.1",
    "parents":["1PAkNtoPUjDnxeKCa3vM-raJ2all1e9zU"]
}

files={
    'data':('metadata',json.dumps(param),'application/json;charset=UTF-8'),
    'file':('Applio-3.1.1',open("F:\softwareSrc\Applio-3.1.1.zip",'rb'),'application/zip')
}

res = requests.post(
    "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
    headers=header,
    files=files
)

if res.status_code == 200:
    print("Done.")
else:
    print("Err.")