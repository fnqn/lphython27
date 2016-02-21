# -*- coding: utf-8 -*-
import os
import time
import json
import subprocess
import settings
import smtplib
from urllib import urlopen
from email.mime.text import MIMEText


def get_microcode_version(serial):
    array_info = {}
    base_url = 'https://atlas-stms.vip.ebay.com/api/v1/arrays/'
    url = base_url + serial
    doc = urlopen(url).read()
    doc = json.loads(doc)
    array_info['serial'] = serial
    array_info['name'] = doc['name']

    if doc['display_model'] == 'VSP':
        array_info['model'] = 'VSP'
    else:
        array_info['model'] = 'G1000'

    array_info['microcode'] = doc['microcode_version'].replace('/', '_')
    print array_info



if __name__ == '__main__':
        get_microcode_version('50360')