from argparse import ArgumentParser, Action
import time

known_drivers = ['local','s3']


class DriverAction(Action):
	def __call__(self, parser, namespace, values, option_string = None):
		driver, destination = values
		namespace.driver = driver.lower()
		namespace.destination = destination
		if driver.lower() not in known_drivers:
			parser.error ("Unknown driver. Available drivers are 'local' & 's3'")


def create_parser():
	parser = ArgumentParser("Backup PostgreSQL database to a local storage device or AWS S3.")
	parser.add_argument("url", help = "URL of database that we want to backup.")
	parser.add_argument("--driver", nargs = 2, required = True, action = DriverAction, help = "How and where we will be storing our backup data.")
	
	return parser


def main():
	import boto3, os
	from pgbackup import pgdump, storage

	parser = create_parser()
	args = parser.parse_args()
	dump = pgdump.dump(args.url)
	timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())

	if args.driver == 's3':
		client = boto3.client('s3')
		file_name = pgdump.dump_file_name(args.url, timestamp)
		print("Backing the database up to", args.destination, "in S3 as", file_name)
		storage.s3(client, dump.stdout, args.destination, file_name)
	else:
		timestamp = time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime())
		name, ext = os.path.splitext(args.destination)
		filename = name + "-" + timestamp + ext
		outfile = open(filename, 'wb')
		print("Backing up the database locally to", filename)
		storage.local(dump.stdout, outfile)

