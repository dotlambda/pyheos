"""Defines tests for HEOS System Commands."""

import pytest

from pyheos import const


@pytest.mark.asyncio
async def test_sign_in(mock_device, heos):
    """Test the sign-in method sends the command as expected."""

    username = "example@example.com"
    password = "example"

    data = {
        const.PARAM_USERNAME: username,
        const.PARAM_PASSWORD: password,
    }
    mock_device.register(const.COMMAND_SIGN_IN, data, "system.sign_in")
    await heos.sign_in(username, password)


@pytest.mark.asyncio
async def test_sign_out(mock_device, heos):
    """Test the sign-in method sends the command as expected."""

    mock_device.register(const.COMMAND_SIGN_OUT, None, "system.sign_out")
    await heos.sign_out()


@pytest.mark.asyncio
async def test_reboot(mock_device, heos):
    """Test the sign-in method sends the command as expected."""

    mock_device.register(const.COMMAND_REBOOT, None, "system.reboot")
    await heos.reboot()
