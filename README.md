**service.pyftpd**
========================
Welcome to the PyFTPd Kodi addon.
For support go to http://forums.tvaddons.co/forums.

**about**
Provides a pyftpd instance for kodi. Runs as a service on kodi startup. Ideal for quick transfer and editing of files to android or ios without need for external services. Supports FTPS on systems with pyOpenSSL.

**settings**
```
Port: Default access is 5021
Use SSL: Requires a certificate in .kodi/userdata/addon_data/service.pyftpd/pyftpd.pem
- To generate:
  1. openssl genrsa -out privkey.pem 2048
  2. openssl req -new -key privkey.pem -out signreq.csr
  3. openssl x509 -req -days 365 -in signreq.csr -signkey privkey.pem -out pyftpd.pem
Username: Access username
Password: ~~SECRET~~
```
