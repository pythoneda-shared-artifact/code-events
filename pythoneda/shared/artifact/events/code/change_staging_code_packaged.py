# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/code/change_staging_code_packaged.py

This file declares the ChangeStagingCodePackaged event.

Copyright (C) 2023-today rydnr's pythoneda-shared-artifact/code-events

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
from pythoneda.shared.code_requests import CodeRequestNixFlake
from pythoneda.shared.code_requests.events import CodePackaged
from typing import List


class ChangeStagingCodePackaged(CodePackaged):
    """
    Represents the moment the code to stage a new change is packaged.

    Class name: ChangeStagingCodePackaged

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        codeRequestNixFlake: CodeRequestNixFlake,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new ChangeStagingCodePackaged instance.
        :param codeRequestNixFlake: The nix flake for the code request.
        :type codeRequestNixFlake: pythoneda.shared.code_requests.CodeRequestNixFlake
        :param previousEventIds: The id of the previous events.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(
            codeRequestNixFlake,
            previousEventIds,
            reconstructedId,
        )


# vim: syntax=python ts=4 sw=4 sts=4 tw=79 sr et
# Local Variables:
# mode: python
# python-indent-offset: 4
# tab-width: 4
# indent-tabs-mode: nil
# fill-column: 79
# End:
