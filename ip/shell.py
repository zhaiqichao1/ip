import os
def installApk(file,package_name,activity):
    print(file)
    # subprocess.call(["adb", "install", file])

    os.system('adb connect 127.0.0.1:16384')
    os.system('adb install ' + file)
    os.system('adb shell am start '+package_name+"/"+activity)

    os.system('mitmdump -p 8899 -s F:/PythonProject/ip/test.py')

    os.system('adb devices')


# adb.exe connect 127.0.0.1:XXXXX