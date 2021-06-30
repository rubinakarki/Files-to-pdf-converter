import subprocess
import requests

url = 'https://s3-us-west-2.amazonaws.com/fuse-ai-resources-dev/onsiteinstructorassignments/5fd6f95c67b0602166815462/5fd6f95d67b0602166815464Screenshot_from_2020-11-20_18-42-48.png'
filename,file_exten = (url.split('/')[-1]).split('.')[0],(url.split('/')[-1]).split('.')[1]
r = requests.get(url) 
 
# import ipdb;ipdb.set_trace()

# storing file locally
with open(f"/home/rubina/uno-test/{filename}.{file_exten}", 'wb') as f:
    f.write(r.content)

# for conversion
convert_command  = f"unoconv -f pdf {filename}.{file_exten}"
subprocess.call(convert_command,shell=True)

upload_to_s3_command = f"aws s3 cp {filename}.pdf s3://fuse-ai-resources-dev/new"
subprocess.call(upload_to_s3_command,shell=True)

# remove file locally
remove_command = f"rm {filename}.{file_exten} && rm {filename}.pdf"
subprocess.call(remove_command,shell=True)
