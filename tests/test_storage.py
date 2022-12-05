from pgbackup import storage
import tempfile
import pytest

@pytest.fixture
def infile():
	f = tempfile.TemporaryFile("r+b")
	f.write(b"Testing")
	f.seek(0)
	return f


# Writing content from one file-like to another file-like object
def test_storing_file_locally(infile):
	outfile = tempfile.NamedTemporaryFile(delete=False)
	storage.local(infile, outfile)

	with open(outfile.name, "rb") as f:
		assert f.read() == b"Testing"


# Writes the contect from oen readable object to the S3 bucket
def test_storing_file_on_s3(mocker, infile):
	client = mocker.Mock()
	storage.s3(client, infile, "bucket", "file-name")

	client.upload_fileobj.assert_called_with(infile, "bucket", "file-name")