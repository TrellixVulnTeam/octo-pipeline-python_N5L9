from enum import Enum


class ActionType(str, Enum):
    LintChecks = "lint-checks"
    Source = "source"
    Consume = "consume"
    Build = "build"
    Layer = "layer"
    CodeChecks = "code-checks"
    UnitTests = "unittests"
    Install = "install"
    SecurityChecks = "security-checks"
    Package = "package"
    E2E = "e2e"
    IntegrationTests = "integration-tests"
    Automation = "automation"
    Deploy = "deploy"
    Mirror = "mirror"
    Destroy = "destroy"
    Activate = "activate"
    Play = "play"
    IACChecks = "iac-checks"
    Execute = "execute"
    GenerateDocs = "generate-docs"
    Upgrade = "upgrade"
    Upload = "upload"
    Download = "download"
    Detect = "detect"
    Verify = "verify"
    Extract = "extract"
