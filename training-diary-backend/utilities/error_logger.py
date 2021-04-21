import traceback
from datetime import datetime


def log_error():
    error_msg = traceback.format_exc().strip("\n")
    print("--------ERROR--------")
    print(error_msg)
    print("---------------------")
    file = open("../error_log.txt", "a")
    file.write(
        "----------START----------" + "\n" +
        "##" + datetime.now().strftime("%Y-%m-%d %H:%M:%S") +
        "\n" + error_msg + "\n" +
        "-----------END-----------" + "\n" + "\n"
    )
    file.close()
