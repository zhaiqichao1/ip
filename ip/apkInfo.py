import os
import re
import subprocess

from shell import installApk
from apkutils import APK
from bs4 import BeautifulSoup


def get_package_name(apk_path):
    apk = APK.from_file(apk_path).parse_resource()
    manifest = apk.get_manifest()
    apk.close()

    soup = BeautifulSoup(manifest, 'xml')
    print()

    ANDROID_HOME = os.getenv('ANDROID_HOME')
    # 获取当前操作系统
    current_os = os.name

    # 根据当前操作系统选择换行符
    if current_os == 'nt':  # Windows系统
        line_break = '\r\n'
    elif current_os == 'posix':  # Linux、Unix-like系统
        line_break = '\n'
    else:  # 其他操作系统，默认使用换行符'\n'
        line_break = '\n'

    # 使用aapt命令获取APK信息 (apk_path：替换为你的APK文件路径)
    # //D:\idea\sdk\build-tools\34.0.0
    command = ['aapt', 'dump', 'badging', apk_path]
    os.chdir("D:/idea/sdk/build-tools/34.0.0".format(ANDROID_HOME))
    result = subprocess.run(command, capture_output=True)

    # 解析输出以获取常见信息
    output = result.stdout.decode('utf-8', 'ignore')
    lines = output.split(line_break)
    print(output)
    #
    package_name = re.search(r"package: name='(.*?)'", lines[0]).group(1)
    try:
        launchable_activity = re.search(r"launchable-activity: name='(.*?)'", output).group(1)
    except AttributeError:
        launchable_activity = soup.findAll("activity-alias")[0]["android:name"]

    version_code = re.search(r"versionCode='(.*?)'", lines[0]).group(1)
    version_name = re.search(r"versionName='(.*?)'", lines[0]).group(1)
    # sdk_version = re.search(r"sdkVersion:'(.*?)'", lines[1]).group(1)

    app_name = ""
    for i in range(0, len(lines)):
        search = re.search(r"application-label:'(.*?)'", lines[i])
        if search == None:
            continue

        if len(app_name) == 0:
            app_name = search.group(1)
            break

    is_arch32 = lines[len(lines) - 2].find("armeabi-v7a") != -1 or lines[len(lines) - 2].find("armeabi") != -1
    is_arch64 = lines[len(lines) - 2].find("arm64-v8a") != -1

    # 打印获取的信息
    print("App Name:", app_name)
    print("Package Name:", package_name)
    print("Version Code:", version_code)
    print("Version Name:", version_name)
    # print("SDK Version:", sdk_version)
    print("是否支持32位:", is_arch32)
    print("是否支持64位:", is_arch64)
    # print("launchable_activity:", launchable_activity)
    installApk(apk_path, package_name, launchable_activity)

# def getActivity(soup):
#     # dom = parseString(manifest)
#     # activities = dom.getElementsByTagName('activity')
#     # # perms = dom.getElementsByTagName('uses-permission')
#
#     # for activity in soup.findAll("activity"):
#         # print(activity)
#     mainactivity = None  # or whatever python null is
#
