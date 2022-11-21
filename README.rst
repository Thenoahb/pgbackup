pgbackup
=========

Command Line Interface for backing up our PostgresSQL database to the local machine or an AWS S3 storage location.

Preparing for Development
_________________________

1. Ensure you have ``pip`` and ``pipenv`` installed and running on your machine.

2. Clone repository: ``git clone git@github.com:Thenoahb/pgbackup.git``

3. ``cd`` into repository.

4. Fetch development dependancies ``make install``

5. Activate virtualenv: ``pipenv shell``

Usage
______

Pass in a full database URL, the storage driver, destination.

S3 Example w/ bucket name:

::
	
	$ pgbackup postgres://NoahDB@192.168.118.129:80/db_one --driver s3 backups

Local Example w/ local path:

::

	$ pgbackup postgres://NoahDB@192.168.118.129:80/db_one --driver local /var/local/db_one/backups

Running Test
_____________

Run test locally using ``make`` if virtual environment is active.

::

	$ make

If virtual environment isn't active, use:

::

	$ pipenv run makea

