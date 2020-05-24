#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
GateKeeper test module

"""
import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gatekeeper import GateKeeper


USER = 'brandon'


class TestGateKeeper(unittest.TestCase):

	# The lock() and unlock() methods are validated through property testing

	def setUp(self):
		self.lockfile = os.path.join(
				os.path.dirname(__file__),
				'testdir',
				'lockfile.txt'
			)
		self.gk = GateKeeper(USER,	self.lockfile)

	def tearDown(self):
		self.gk.unlock()

	def test_lock_is_acquired_returns_none(self):
		self.assertIsNone(self.gk.lock_is_acquired)

	def test_lock_is_acquired_returns_true(self):
		self.gk.lock()
		self.assertTrue(self.gk.lock_is_acquired)

	def test_owner_returns_none(self):
		self.assertEqual(self.gk.owner, None)

	def test_owner_returns_user(self):
		self.gk.lock()
		self.assertEqual(self.gk.owner, USER)


if __name__ == '__main__':
	unittest.main(verbosity=2)