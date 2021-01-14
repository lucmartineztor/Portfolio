import os
os.system("ps -ef | grep 'run.sh'")
os.system("pgrep -f 'run.sh' | xargs kill -9")
os.system("sh run.sh")
