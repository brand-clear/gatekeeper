#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class GateKeeper(object):
	"""
	A lockfile controller that aims to support multi-user I/O operations over a network file system.

	Attributes
	----------
	lock_is_acquired
	owner

	Parameters
	----------
	username : str
		Unique id that is appended to `lockfile` after acquisition.
	lockfile : str
		Absolute path to lockfile.

	Notes
	-----
	I/O operations should be called only after successfully acquiring the lockfile and prior to releasing the lockfile.

	"""
	def __init__(self, username, lockfile):
		self._username = username
		self._unlocked_path = lockfile
		self._filename = os.path.basename(self._unlocked_path)
		self._locked_path = '%s.%s' % (self._unlocked_path, self._username)

	@property
	def lock_is_acquired(self):
		"""True or None: Confirmation that lockfile is acquired."""
		if os.path.exists(self._locked_path):
			return True

	@property
	def owner(self):
		"""str or None: The lockfile owner."""
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
		bool
			An indication of lockfile acquisition success.

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
		bool
			An indication of lockfile releasal success.
			
		"""
		try:
			os.rename(self._locked_path, self._unlocked_path)
		except OSError:
			return False
		else:
			return True


if __name__ == '__main__':
	pass

