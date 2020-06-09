"""
gatekeeper test  module

"""
import os
import sys
import unittest
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from gatekeeper.gatekeeper import GateKeeper


class TestGateKeeper(unittest.TestCase):

	# lock() and unlock() methods are validated through testing dependent
	# methods. If any dependent method fails, it is likely that lock() or
	# unlock() is the reason.

	def setUp(self):
		self.lockfile = os.path.join(
				os.path.dirname(__file__),
				'testdir',
				'lockfile.txt'
			)
		self.gk = GateKeeper('brandon',	self.lockfile)

	def tearDown(self):
		self.gk.unlock()

	def test_lock_is_acquired_returns_none(self):
		self.assertIsNone(self.gk.lock_is_acquired)

	def test_lock_is_acquired_returns_true(self):
		self.gk.lock()
		self.assertTrue(self.gk.lock_is_acquired)

	def test_owner_returns_none(self):
		self.assertEqual(self.gk.owner, None)

	def test_owner_returns_brandon(self):
		self.gk.lock()
		self.assertEqual(self.gk.owner, 'brandon')


if __name__ == '__main__':
	unittest.main(verbosity=2)