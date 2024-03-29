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

from smartcalserver.app.vtimezone import TimezoneForeignData, TimezoneData, Timezone
import pytest

def test_instantiateInvalidTimezoneForeignData():
	with pytest.raises(Exception):
		timezoneforeigndata_instance = TimezoneForeignData()

def test_instantiateTimezoneData():
	timezonedata_instance = TimezoneData()
	assert timezonedata_instance is not None

def test_instantiateTimezone():
	timezone_instance = Timezone()
	assert timezone_instance is not None
