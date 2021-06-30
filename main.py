import subprocess
import requests

url = 'https://s3-us-west-2.amazonaws.com/fuse-ai-resources-dev/onsiteinstructorassignments/5fd6f95c67b0602166815462/5fd6f95d67b0602166815464Screenshot_from_2020-11-20_18-42-48.png'
filename = url.split('/')[-1]
r = requests.get(url)  

# storing file locally
with open(f"/home/rubina/uno-test/{filename}", 'wb') as f:
    f.write(r.content)

# for conversion
convert_command  = f"unoconv -f pdf {filename}"
subprocess.call(convert_command,shell=True)

# remove file locally
remove_command = f"rm {filename}"
subprocess.call(remove_command,shell=True)

# command = f' cat {res.content} | unoconv --output=out.pdf --stdin'
# cat 160930-artificial-intelligence-template-16x9.pptx | unoconv --output=out.pdf --stdin
# unoconv -o /home/rubina/listener/abc.pdf -f pdf 160930-artificial-intelligence-template-16x9.pptx