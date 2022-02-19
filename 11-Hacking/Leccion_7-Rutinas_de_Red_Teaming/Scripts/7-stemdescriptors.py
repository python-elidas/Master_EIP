from stem.descriptor.remote import DescriptorDownloader
from stem.version import Version
downloader = DescriptorDownloader()
for desc in downloader.get_server_descriptors():
	if desc.tor_version < Version('0.4.0'):
		print(desc.address + " - "+str(desc.tor_version))
		if desc.contact:
			print(' %s' % (desc.contact.decode("utf-8", "replace")))
