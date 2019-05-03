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
import os
import xbmc
from threading import Thread
from pyftpdlib.servers import ThreadedFTPServer
from pyftpdlib.authorizers import DummyAuthorizer
from commoncore import *
from commoncore import kodi

test = xbmc.__version__.split('.')
is_depricated = True if int(test[1]) < 19  else False
class FTPService():
	def __init__(self, *args, **kwargs):
		self.ftp_root = kodi.vfs.translate_path(kodi.get_setting('root_directory'))
		self.ftp_log = kodi.vfs.join(kodi.get_profile(), "pyftpd.log")
		self.cert_file = vfs.join(kodi.get_profile(), "pyftpd.pem")
		if not vfs.exists(self.cert_file):
			vfs.cp(vfs.join(kodi.get_path(), "pyftpd.pem"), self.cert_file)
	
	def start(self):
		class Monitor(xbmc.Monitor):
			def onSettingsChanged(self):
				pass
		monitor = Monitor()
		kodi.log("Service Starting...")
		authorizer = DummyAuthorizer()
		authorizer.add_user(kodi.get_setting('ftp_user'), kodi.get_setting('ftp_pass'), self.ftp_root, perm='elradfmwMT')
		if kodi.get_setting('use_ssl') == 'true':
			from pyftpdlib.handlers import TLS_FTPHandler as handler
			handler.certfile = self.cert_file
		else:
			from pyftpdlib.handlers import FTPHandler as handler

		handler.banner = "PyFTPd ready."
		handler.authorizer = authorizer
		address = ('', kodi.get_setting('server_port'))
		import logging
		logging.basicConfig(filename=self.ftp_log, level=logging.INFO)
		self.ftpd = ThreadedFTPServer(address, handler)
		self.ftpd.max_cons = 256
		self.ftpd.max_cons_per_ip = 5
		self.server = Thread(target=self.ftpd.serve_forever)
		self.server.start()
		
		if is_depricated:
			while not xbmc.abortRequested:
				xbmc.sleep(1000)
		else:
			while not monitor.abortRequested():
				xbmc.sleep(1000)
				
		self.shutdown()
	
	
	def shutdown(self):
		kodi.log("Service Stopping...")
		self.ftpd.close_all()
		self.server.join()


if __name__ == '__main__':
	server = FTPService()
	server.start()
