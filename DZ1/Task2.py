import subprocess
import string


# !/bin/bash
# result=$(cat /etc/os-release)
# if [[ $result = *"22.04.3"* && *"jammy"* && $? == 0 ]];
# then echo "SUCCESS"
# else echo "FAIL"
# fi

def checkVersion():
    result = subprocess.run("cat /etc/os-release",
                            shell=True, stdout=subprocess.PIPE,
                            encoding="utf-8")

    for item in str(result).split(string.punctuation):
        if "jammy" in item and "22.04.3" in result.stdout and result.returncode == 0:
            print(str(result).split(string.punctuation))
            print("SUCCESS")
            return True
        else:
            print(str(result).split(string.punctuation)[0])
            print("FAIL")
            return False


checkVersion()
