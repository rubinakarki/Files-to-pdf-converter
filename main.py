import subprocess

file_name = '/home/rubina/Downloads/1611868976156.jpeg'
command  = f"unoconv -f pdf {file_name}"
subprocess.call(command,shell=True)