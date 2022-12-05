from argparse import ArgumentParser, Action


class DriverAction(Action):
	def __call__(self, parser, namespace, values, option_string = None):
		driver, destination = values
		namespace.driver = driver.lower()
		namespace.destination = destination
		if driver.lower() == "local" or driver.lower() == "s3":
			pass
		else:
			parser.error ("Unknown driver. Available drivers are 'local' &'s3'")


def create_parser():
	parser = ArgumentParser("Backup PostgreSQL database to a local storage device or AWS S3.")
	parser.add_argument("url", help = "URL of database that we want to backup.")
	parser.add_argument("--driver", nargs = 2, required = True, action = DriverAction, help = "How and where we will be storing our backup data.")
	
	return parser