import info
from Package.CMakePackageBase import *


class subinfo(info.infoclass):
    def setTargets(self):
        for ver in ['2.1.0']:
            self.targets[ver] = 'https://download.kde.org/stable/maui/mauikit-filebrowsing/%s/mauikit-filebrowsing-%s.tar.xz' % (ver, ver)
            self.archiveNames[ver] = 'mauikit-filebrowsing-%s.tar.gz' % ver
            self.targetInstSrc[ver] = 'mauikit-filebrowsing-%s' % ver

        self.description = "mauikit file browsing"
        self.defaultTarget = '2.1.0'

    def setDependencies(self):
        self.buildDependencies["virtual/base"] = None
        self.buildDependencies["kde/frameworks/extra-cmake-modules"] = None
        self.runtimeDependencies["kde/maui/mauikit"] = None
        self.runtimeDependencies["libs/qt5/qtbase"] = None
        self.runtimeDependencies["kde/frameworks/tier1/ki18n"] = None
        self.runtimeDependencies["kde/frameworks/tier1/kcoreaddons"] = None


class Package(CMakePackageBase):
    def __init__(self, **args):
        CMakePackageBase.__init__(self)
