import os


def create_folder(directory, folder_name):
    # Create the full path for the new folder
    new_folder_path = os.path.join(directory, folder_name)

    # Check if the folder already exists
    if not os.path.exists(new_folder_path):
        # Create the new folder
        os.makedirs(new_folder_path)
        print(f"Folder '{folder_name}' created successfully in '{directory}'.")
    else:
        print(f"Folder '{folder_name}' already exists in '{directory}'.")


voiceActorArr = [
    "arjun",
    "keerthySuresh",
    "mysskin",
    "siddharth",
    "sjSuriya",
    "andrea",
    "berlin",
    "denver",
    "ladyPloice",
    "nairobi",
    "pelurmo",
    "policeOffice",
    "tokyo",
]


directory = r"F:\softwareSrc\Applio-3.1.1\rvc\Voicemodels\download"


for actor in voiceActorArr:
    print(actor)
    create_folder(directory, actor)
