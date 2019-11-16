"""
Handles the SQL export to ipboard v3.1.4
"""
from django.template.loader import render_to_string
from django.utils.encoding import smart_str
from django.utils.translation import activate

from zetaboardsbackup.forum.backends.base import BaseExporter
from zetaboardsbackup.forum.models import Forum, Thread, Post, User
from zetaboardsbackup import log
from multiprocessing import Process

import gc

def export_users(items, begin, end, filename):
    log.info('Exporting Posts: Begin ' + str(begin) + ' - End: ' + str(end))
    context = {'posts': items[begin:end]}
    rendered = render_to_string('backends/xenforo/export_posts.sql', context)
    f = open(filename, 'w+')
    f.write(smart_str(rendered))
    f.close()

class XenforoExporter(BaseExporter):

    def export_users(self):
        activate('en')
        context = {'users': User.objects.all()}
        rendered = render_to_string('backends/xenforo/export_users.sql', context)
        return rendered
    
    def export_forums(self):
        activate('en')
        context = {'forums': Forum.objects.all()}
        rendered = render_to_string('backends/xenforo/export_forums.sql', context)
        return rendered

    def export_threads(self):
        activate('en')
        context = {'threads': Thread.objects.all()}
        rendered = render_to_string('backends/xenforo/export_threads.sql', context)
        return rendered

    def export_posts(self):
        activate('en')
        items = Post.objects.all()
        count = len(items)
        blockCount = 500
        blockSize = count / blockCount
        log.info('Exporting Posts: Count: ' + str(count) + ' - blockSize: ' + str(blockSize))
        for i in range(0,(blockCount - 1)):
            begin = blockSize * i
            end = blockSize * (i + 1)
            p = Process(target=export_users, args=(items,begin,end,'output' + str(i) + '.sql'))
            p.start()
            p.join()
            log.info('Exporting Posts: Begin ' + str(begin) + ' - End: ' + str(end) + ' -- COMPLETE')


        begin = blockSize * blockCount
        context = {'posts': items[begin:]}
        rendered = render_to_string('backends/xenforo/export_posts.sql', context)
        f = open('output_end.sql', 'w+')
        f.write(smart_str(rendered))
        f.close()
        return rendered


EXPORTER = XenforoExporter
