from conans import ConanFile, tools


class Fcitx5QtConan(ConanFile):
    name = "fcitx5-qt"
    version = "0.0.0"
    build_version = "20181104-1"
    settings = "os", "arch"
    description = "Qt library and IM module for fcitx5"
    url = "https://github.com/altairwei/conan-fcitx5-qt.git"
    homepage = "https://gitlab.com/fcitx/fcitx5-qt"
    license = "BSD"
    build_policy="missing"

    def configure(self):
        if self.settings.os != "Linux":
            raise Exception("Only Linux supported for fcitx5-qt")
        if self.settings.arch not in ["x86_64"]:
            raise Exception("Only x86_64 supported for fcitx5-qt")

    def build(self):
        url = "https://www.archlinux.org/packages/community/{arch}/fcitx5-qt/download".format(
            arch = self.settings.arch
        )
        tools.download(url, "fcitx5-qt.pkg.tar.xz")
        self.run("tar -xf fcitx5-qt.pkg.tar.xz")

    def package(self):
        self.copy("*", src="usr", keep_path=True)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.libs = ["fcitx-qt5"]
