#!/usr/bin/python3

import pytest, subprocess
from pgbackup import pgdump

url = "postgres://NoahDB:cit483@10.2.56.123:80/db_one"

#  Utilize pg_dump with the database URL.
def test_dump_calls_pg_dump(mocker):
	mocker.patch("subprocess.Popen")
	assert pgdump.dump(url)
	subprocess.Popen.assert_called_with(["pg_dump", url], stdout = subprocess.PIPE)


#  pgdump.dump returns a reasonable error if pg_dump isn't installed.
def test_dump_handles_oserror(mocker):
	mocker.patch("subprocess.Popen", side_effect = OSError("No such file."))
	with pytest.raises(SystemExit):
		pgdump.dump(url)


# pgdump.db_file_name returns the name of the database
def test_dump_file_name_without_timestamp():
	assert pgdump.dump_file_name(url) == "db_one.sql" 


# pgdump.db_file_name returns the name of the database
def test_dump_file_name_with_timestamp():
	timestamp = "2022-12-05T13:24:50"

	assert pgdump.dump_file_name(url, timestamp) == "db_one-" + timestamp + ".sql"