import subprocess
import string

#!/bin/bash
#result=$(cat /etc/os-release)
#if [[ $result = *"22.04.3"* && *"jammy"* && $? == 0 ]];
#then echo "SUCCESS"
#else echo "FAIL"
#fi

def checkVersion():
    result = subprocess.run("cat /etc/os-release",
                            shell=True, stdout=subprocess.PIPE,
                            encoding="utf-8")

    if "jammy" in result.stdout and "22.04.3" in result.stdout and result.returncode == 0:
        print(str(result))
        print("SUCCESS")
        return True
    else:
        print("FAIL")
        return False

checkVersion()



