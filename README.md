# gatekeeper
A lockfile controller that aims to support multi-user I/O operations over a network file system.

## Purpose
`gatekeeper` was created to address the issue of multiple users accessing the same shared data over a network file system. This is more of a "best shot" than a perfect solution.

## Usage
This system is built upon the idea that every data file or every set of data files is guarded by a lockfile. In order to read or write to the data file, one must first acquire rights to the lockfile. `gatekeeper` aims to handle the acquisition and releasal of the lockfile.
```
from gatekeeper.gatekeeper import GateKeeper

lock = GateKeeper('username', 'path_to_lockfile')
if lock.lock():
    # lockfile has been acquired
    # perform CRUD operations
    lock.unlock()
```
