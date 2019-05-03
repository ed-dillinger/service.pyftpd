# -*- coding: utf-8 -*-

'''*
	Copyright (C) 2017 EDDillinger
	Initial code adapted from DudeHere

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
*'''

from commoncore.enum import enum
from commoncore import kodi
def utf8(string):
	try: 
		string = u'' + string
	except UnicodeEncodeError:
		string = u'' + string.encode('utf-8')
	except UnicodeDecodeError:
		string = u'' + string.decode('utf-8')
	return string

#ARTWORK = kodi.vfs.join(kodi.get_profile(), 'resources/artwork')
CACHE_PATH = kodi.vfs.join(kodi.get_profile(),'cache')
#VIEWS = enum(DEFAULT=500, LIST=50, BIGLIST=51, THUMBNAIL=500, SMALLTHUMBNAIL=522, FANART=508, POSTERWRAP=501, MEDIAINFO=504, MEDIAINFO2=503, MEDIAINFO3=515, WIDE=505, LIST_DEFAULT=50, TV_DEFAULT=50, MOVIE_DEFAULT=50, SEASON_DEFAULT=50, EPISODE_DEFAULT=50)
#UNAIRED_COLOR = 'maroon'

if not kodi.vfs.exists(CACHE_PATH): kodi.vfs.mkdir(CACHE_PATH, recursive=True)
