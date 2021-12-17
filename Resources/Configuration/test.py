import os


class Demo:
    @staticmethod
    def remove_app():
        os.system("adb uninstall io.lifestyle.plus")
