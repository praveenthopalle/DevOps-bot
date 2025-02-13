from app.pkgs.knowledge.app_info_interface import AppInfoInterface

class AppInfoPro(AppInfoInterface):
    def getServiceLib(self, appID, serviceName):
        # The current version does not support this feature
        return "", False

    def getServiceStruct(self, appID, serviceName):
        # The current version does not support this feature
        return "", False

    def getServiceSpecification(self, appID, serviceName, LibName):
        # The current version does not support this feature
        return "", False

    def analyzeService(self, gitPath):
        # The current version does not support this feature
        return "", False