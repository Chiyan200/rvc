import json
import zipfile

# pip install -U "huggingface_hub[cli]" module command
# huggingface-cli login --token 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 -login command
# huggingface-cli download ChiyanChandru/VocieModel --repo-type=dataset --local-dir=F:\Applio-3.1.1\Applio-3.1.1\Voicemodels\download --file downloda command 
# huggingface-cli upload ChiyanChandru/VocieModel F:\softwareSrc\Applio-3.1.1\rvc\Voicemodels\upload\final\mysskin.zip --upload

def extract_zip(zip_path, extract_to):
    """
    Extract all contents of a zip file to a specified directory.

    :param zip_path: Path to the zip file.
    :param extract_to: Directory where the contents will be extracted.
    """
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
        print(f"All files extracted to {extract_to}")

# Example usage
zip_file_path = r'F:\Applio-3.1.1\Applio-3.1.1\Voicemodels\download\miniLog.zip'
extract_to_directory = r'F:\Applio-3.1.1\Applio-3.1.1\Voicemodels\download'
extract_zip(zip_file_path, extract_to_directory)
 