# Copyright (C) 2022 Innovate for Vegas Foundation
# 
# This file is part of be-smart-calendar-server-py.
# 
# be-smart-calendar-server-py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# be-smart-calendar-server-py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with be-smart-calendar-server-py.  If not, see <http://www.gnu.org/licenses/>.


from smartcalserver.caldav.base import BaseCalDAVHandler

def test_InstantiateBaseCalDAVHandler():
	BaseCalDAVHandler_instance = BaseCalDAVHandler()
	assert BaseCalDAVHandler_instance is not None

def test_TestValidRequest():
	req = dict(path='/test/path')
	BaseCalDAVHandler_instance = BaseCalDAVHandler()
	BaseCalDAVHandler_instance.parse_request(req)
	assert BaseCalDAVHandler_instance.status('request_valid') is True
