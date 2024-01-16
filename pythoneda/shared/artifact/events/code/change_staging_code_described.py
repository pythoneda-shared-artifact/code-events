# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/code/change_staging_code_described.py

This file declares the ChangeStagingCodeDescribed event.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/code/events

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from pythoneda.shared.code_requests import CodeRequest
from pythoneda.shared.code_requests.events import CodeDescribed
from typing import List


class ChangeStagingCodeDescribed(CodeDescribed):
    """
    Represents the moment the code to stage a new change is described.

    Class name: ChangeStagingCodeDescribed

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        codeRequest: CodeRequest,
        changeStagingCodeRequestId: str = None,
        reconstructedId: str = None,
        reconstructedPreviousEventIds: List[str] = None,
    ):
        """
        Creates a new ChangeStagingCodeDescribed instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :param changeStagingCodeRequestId: The id of previous event.
        :type changeStagingCodeRequestId: str
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        :param reconstructedPreviousEventIds: The id of the previous events, if an external event
        is being reconstructed.
        :type reconstructedPreviousEventIds: List[str]
        """
        super().__init__(
            codeRequest,
            changeStagingCodeRequestId,
            reconstructedId,
            reconstructedPreviousEventIds,
        )
