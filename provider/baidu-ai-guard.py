from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError

class BaiduAiGuardProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        access_key = credentials.get("access_key")
        if not access_key:
            raise ToolProviderCredentialValidationError("access_key is required")

        secret_key = credentials.get("secret_key")
        if not secret_key:
            raise ToolProviderCredentialValidationError("secret_key is required")

        try:
            return
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
