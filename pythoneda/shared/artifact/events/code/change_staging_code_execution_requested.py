# vim: set fileencoding=utf-8
"""
pythoneda/shared/artifact/events/code/change_staging_code_execution_requested.py

This file declares the ChangeStagingCodeExecutionRequested event.

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
from pythoneda.shared.code_requests import CodeRequest
from pythoneda.shared.code_requests.events import CodeExecutionRequested
from typing import List


class ChangeStagingCodeExecutionRequested(CodeExecutionRequested):
    """
    Represents the moment someone requests the execution of the code to stage a new change.

    Class name: ChangeStagingCodeExecutionRequested

    Responsibilities:
        - Wraps all contextual information of the event.

    Collaborators:
        - None
    """

    def __init__(
        self,
        codeRequest: CodeRequest,
        previousEventIds: List[str] = None,
        reconstructedId: str = None,
    ):
        """
        Creates a new ChangeStagingCodeExecutionRequested instance.
        :param codeRequest: The code request.
        :type codeRequest: pythoneda.shared.code_requests.CodeRequest
        :param previousEventIds: The id of previous events, if any.
        :type previousEventIds: List[str]
        :param reconstructedId: The id of the event, if it's generated externally.
        :type reconstructedId: str
        """
        super().__init__(
            codeRequest,
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
