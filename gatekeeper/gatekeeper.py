

import os


class GateKeeper(object):
	"""The GateKeeper Class supports multi-user I/O operations over a network 
	file system by enforcing a lockfile buffer to sensitive data.

	The I/O operations themselves are to be carried out after acquiring the
	lockfile (via lock()) and prior to releasing the lockfile to other users
	(via unlock()).

	Parameters
	----------
	username : str
		Unique id that is appended to `lockfile` during a locking
		operation, signifying ownership.
	lockfile : str
		Absolute path to lockfile.

	Attributes
	----------
	lock_is_acquired
	owner

	"""
	def __init__(self, username, lockfile):
		self._username = username
		self._unlocked_path = lockfile
		self._filename = os.path.basename(self._unlocked_path)
		self._locked_path = '%s.%s' % (self._unlocked_path, self._username)

	@property
	def lock_is_acquired(self):
		"""
		Returns
		-------
		True or None
			If True, self._username has lockfile ownership.

		"""
		if os.path.exists(self._locked_path):
			return True

	@property
	def owner(self):
		"""
		Returns
		-------
		str or None
			Current lockfile owner.

		"""
		for f in os.listdir(os.path.dirname(self._locked_path)):
			if self._filename in f:
				try:
					return f.split('.')[2]
				except IndexError:
					return None

	def lock(self):
		"""Attempt to acquire lockfile.
		
		Returns
		-------
		True or False
			Acquisition state.

		"""
		try:
			os.rename(self._unlocked_path, self._locked_path)
		except OSError:
			return False
		else:
			return True

	def unlock(self):
		"""Attempt to release lockfile.
		
		Returns
		-------
		True or False
			Releasal state.
			
		"""
		try:
			os.rename(self._locked_path, self._unlocked_path)
		except OSError:
			return False
		else:
			return True



if __name__ == '__main__':
	pass
