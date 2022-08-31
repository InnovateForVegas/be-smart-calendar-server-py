# Copyright (C) 2022 Code for Vegas Foundation
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

from smartcalserver.app.user import UserForeignData, UserData, User

def test_instantiateUserForeignData():
	userforeigndata_instance = UserForeignData()
	assert userforeigndata_instance is not None

def test_instantiateUserData():
	userdata_instance = UserData()
	assert userdata_instance is not None

def test_instantiateUser():
	user_instance = User()
	assert user_instance is not None