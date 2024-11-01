import re
import yaml  # Ensure PyYAML is installed
from synapse.module_api import ModuleApi
from synapse.spam_checker_api import RegistrationBehaviour
from typing import Optional, Collection, Tuple

class EmailBlacklistModule:
    def __init__(self, config, api: ModuleApi):
        self.api = api
        # Load configuration if it's provided as a file path
        if isinstance(config, str):
            with open(config, "r") as f:
                config = yaml.safe_load(f)

        # Retrieve the email blacklist from the config, defaulting to an empty list
        self.email_blacklist = config.get("email_blacklist", [])

        # Register the spam check for registration
        self.api.register_spam_checker_callbacks(
            check_registration_for_spam=self.check_registration_for_spam
        )

    async def check_registration_for_spam(
        self,
        email_threepid: Optional[dict],
        username: Optional[str],
        request_info: Collection[Tuple[str, str]],
        auth_provider_id: Optional[str] = None,
    ) -> RegistrationBehaviour:
        """
        Checks if the email in the registration data is blacklisted.
        Returns RegistrationBehaviour.DENY if the registration should be blocked,
        otherwise RegistrationBehaviour.ALLOW.
        """
        # Extract email from the email_threepid dictionary, if present
        email = email_threepid.get("address") if email_threepid else None

        # Check if the email matches any pattern in the blacklist
        if email:
            for pattern in self.email_blacklist:
                if re.search(pattern, email):
                    return RegistrationBehaviour.DENY  # Block registration

        return RegistrationBehaviour.ALLOW  # Allow registration
