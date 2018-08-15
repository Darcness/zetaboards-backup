"""
All exporter classes should subclass from this base exporter.
"""

from django.utils.encoding import smart_str
import gc

from zetaboardsbackup import log

class BaseExporter(object):
    """
    The base SQL exporter, subclass from this.
    """

    def export(self):
        """
        Runs the export process.
        """
        log.info("Exporter initialised.")


        output = u""
        output += self.export_users()
        f = open('output_users.sql', 'w+')
        f.write(smart_str(output))
        f.close()
        log.info("Exported users")
        
        output = self.export_forums()
        f = open('output_forums.sql', 'w+')
        f.write(smart_str(output))
        f.close()
        log.info("Exported forums")

        output = self.export_threads()
        f = open('output_threads.sql', 'w+')
        f.write(smart_str(output))
        f.close()
        log.info("Exported threads")

        
        output = self.export_posts()
        log.info("Exported posts")
        """
        f = open('output.sql', 'a+')
        f.write(smart_str(output))
        f.close()
        """
        log.info("Export File Complete")

    def export_users(self):
        raise NotImplementedError

    def export_forums(self):
        raise NotImplementedError

    def export_threads(self):
        raise NotImplementedError

    def export_posts(self):
        raise NotImplementedError
