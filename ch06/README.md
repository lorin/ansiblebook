# Ansible playbooks for deploying a Mezzanine application

The code for this chapter shows how to use Ansible to deploy a
[Mezzanine][1] site into a Vagrant box.

## Before running the playbook

Don't forget to do the following:

    cd playbooks
    cp secrets.yml.example secrets.yml

## Running the playbook

Then you can deploy Mezzanine by doing:

    vagrant up
    ansible-playbook mezzanine.yml


Then point your browser to: <http://192.168.33.10.xip.io> or
<https://www.192.168.33.10.xip.io>. You'll get a security warning if you use the
https site since it's a self-signed certificate, this is normal.

[1]: http://mezzanine.jupo.org
