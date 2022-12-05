#!/usr/bin/python3

import pytest 
from pgbackup import cli

url = "postgres://bob:password@example.com:5432/db_one" 
#url = "postgres://NoahDB:cit483@192.168.118.129:80/db_one"


@pytest.fixture
def parser():
	parser = cli.create_parser()
	return parser


#  Without a specified driver the parser will exit,
def test_parser_without_driver(parser): 
	with pytest.raises(SystemExit):
		parser.parse_args([url])

#  With a driver but no destination the parser will exit.
def test_parser_with_driver(parser):
	with pytest.raises(SystemExit):
		parser.parse_args([url, "--driver", "local"])


#  Successfull argument parse if we have a driver and a destination.
def test_parser_with_driver_and_destination(parser):
	args = parser.parse_args([url, "--driver", "local", "/some/path"])
	assert args.url == url
	assert args.driver == "local"
	assert args.destination == "/some/path"


#  The parser will exit if the driver name is does match our two expected options. 
def test_parser_with_unknown_drivers(parser):
	args = parser.parse_args([url, "--driver", "s3", "/some/path"])
	assert args.driver.lower() == "local" or args.driver.lower() == "s3"