import requests
import sys
from time import sleep

def regUploadRes(apiUrl, marketCode, version, buildType, buildNum, adminToken):
    url = apiUrl+"/jenkinsManager/build"
    data={'token': adminToken,'marketCode': marketCode, 'version': version, 'buildType': buildType, 'buildNum': buildNum}
    print("Request: ", url, dict(data.items()))
    for i in range(5):
        try:
            response = requests.post(url, data=data)
        except:
            print("post failed , %d try"%(i+1))
            sleep(5)
            continue
        break
    print("Response: ", response.json())

    return response.ok


def main():
    if len(sys.argv) < 7:
        print("Usage: apiUrl marketCode version buildType buildNum adminToken")
        return -1

    apiUrl      = sys.argv[1]
    marketCode  = sys.argv[2]
    version     = sys.argv[3]
    buildType   = sys.argv[4]
    buildNum    = sys.argv[5]
    adminToken  = sys.argv[6]

    if not regUploadRes(apiUrl, marketCode, version, buildType, buildNum, adminToken) :
        print("Register Upload Resources: Fail")
        return -1

    print("Register Upload Resources Sucessfully!\n")
    print("Notice: Successfully processed")

    return 0


if __name__ == "__main__":
    main()
