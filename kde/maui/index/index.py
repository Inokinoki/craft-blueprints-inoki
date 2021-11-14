import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['2.1.0']:
            self.targets[ver] = 'https://download.kde.org/stable/maui/index/%s/index-%s.tar.xz' % (ver, ver)
            self.archiveNames[ver] = 'index-%s.tar.gz' % ver
            self.targetInstSrc[ver] = 'index-%s' % ver

        self.description = "mauikit Index file browser"
        self.defaultTarget = '2.1.0'

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols"] = None
        self.runtimeDependencies["libs/qt5/qtquickcontrols2"] = None
        self.runtimeDependencies["kde/maui/mauikit"] = None
        self.runtimeDependencies["kde/maui/mauikitfilebrowsing"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None
        self.runtimeDependencies["kde/frameworks/tier1/karchive"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
