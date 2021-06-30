import subprocess
import requests

url = 'https://s3-us-west-2.amazonaws.com/fuse-ai-resources-dev/onsiteinstructorassignments/60da9d683aa49a40cd061c2d/60da9d683aa49a40cd061c2fscrum.docx'

foldername,filename,file_exten = url.split('/')[5],(url.split('/')[-1]).split('.')[0],(url.split('/')[-1]).split('.')[1]
r = requests.get(url) 

# storing file locally
with open(f"/home/rubina/uno-test/{filename}.{file_exten}", 'wb') as f:
    f.write(r.content)

# for conversion
convert_command  = f"unoconv -f pdf --output={filename}3.pdf {filename}.{file_exten}"
subprocess.call(convert_command,shell=True)

upload_to_s3_command = f"aws s3 cp {filename}3.pdf s3://fuse-ai-resources-dev/onsiteinstructorassignments/{foldername}/converted/"
subprocess.call(upload_to_s3_command,shell=True)

# boto3

# remove file locally
remove_command = f"rm {filename}.{file_exten} && rm {filename}3.pdf"
subprocess.call(remove_command,shell=True)

output_url = f"https://s3-us-west-2.amazonaws.com/fuse-ai-resources-dev/onsiteinstructorassignments/{foldername}/converted/{filename}3.pdf"
print(output_url)

