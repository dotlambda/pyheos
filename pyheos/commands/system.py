"""Define the HEOS System Commands."""

from pyheos import const

from typing import Optional


class SystemCommands:
    """Encapsulates HEOS System Commands."""

    def __init__(self, connection):
        """Init the command wrapper."""
        self._connection = connection

    async def register_for_change_events(self, enable: bool = True) -> None:
        """Register for Change Events."""
        params = {const.PARAM_ENABLE: const.VALUE_ON if enable else const.VALUE_OFF}
        await self._connection.command(const.COMMAND_REGISTER_FOR_CHANGE_EVENTS, params)

    async def check_account(self) -> Optional[str]:
        """Return the logged in username."""
        response = await self._connection.command(const.COMMAND_ACCOUNT_CHECK, None)
        if response.has_message(const.PARAM_SIGNED_IN):
            return response.get_message(const.PARAM_USERNAME)
        return None

    async def sign_in(self, username: str, password: str) -> None:
        """Sign in to the HEOS account using the provided credential."""
        params = {const.PARAM_USERNAME: username, const.PARAM_PASSWORD: password}
        await self._connection.command(const.COMMAND_SIGN_IN, params)

    async def sign_out(self) -> None:
        """Sign out of the HEOS account."""
        await self._connection.command(const.COMMAND_SIGN_OUT, None)

    async def heart_beat(self) -> None:
        """Perform heart beat command."""
        await self._connection.command(const.COMMAND_HEART_BEAT, None)

    async def reboot(self) -> None:
        """Reboot the HEOS devices that is currently connected."""
        await self._connection.command(const.COMMAND_REBOOT, None)
