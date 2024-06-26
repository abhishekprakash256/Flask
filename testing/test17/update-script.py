"""
The script to update branch , kill the server , push the database values and run the server again
"""

"""
#print('returncode:', result.returncode)
The commands to run 

git pull 
ps aux | grep flask
kil pid

cd mongo
python3 bulk_data_insertion.py

cd .. 
flask run --host=0.0.0.0 --port=5000 > output.log 2>&1 & disown

"""


import subprocess
import os


# Running a command to pull the latest git files
git_pull = subprocess.run(['git', 'pull'], capture_output=True, text=True)

print('stdout:', git_pull.stdout)


#kill the flask server 
flask_process = subprocess.run('ps aux | grep flask', shell=True, capture_output=True, text=True)


flask_pid = flask_process.stdout[10:16]

print(flask_pid)

#store the originonal directory 
original_directory = os.getcwd()


#kill the flask process
kill_flask_process = subprocess.run(['kill', flask_pid], capture_output=True, text=True)

#print(kill_flask_process.returncode)

#injets the dataset for mongo db 

injest_data = subprocess.run(['cd mongo && python3 bulk_data_insertion.py'], shell=True, capture_output=True, text=True, check=True)

print(injest_data.stdout)


#change the dir again
os.chdir(original_directory)

#run the flask server again 


run_server = subprocess.run('nohup flask run --host=0.0.0.0 --port=5000 > output.log 2>&1 &', shell=True, check=True)
if run_server:
    print("Flask server started succesfully")

else:
    print("Failed to start Flask server")
