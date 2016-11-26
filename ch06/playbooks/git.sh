#!/bin/bash
ansible web -m git -a "repo=git@github.com:lorin/mezzanine-example.git dest=/home/vagrant/mezzanine-example/project accept_hostkey=yes"
