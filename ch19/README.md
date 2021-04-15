# Tower

This project creates 3 Centos7 VMs with Vagrant/Virtualbox. The ansible provisioner will install Tower from your local ~/Downloads/.

## Usage:
- If you have a Mac with Homebrew, then you can install what's in the Brewfile with `brew bundle`
- Open the web page [https://www.ansible.com/zero-to-100](https://www.ansible.com/zero-to-100)
- Set `tower_name: ansible-automation-platform-setup-bundle-1.2.1-1`
- Create a virtualenv with: `source init.rc`
- Update the passwords and encrypt `group_vars/vagrant/vars.yml`
- Provision Ansible Tower: `vagrant up`
- open http://server03 for Tower
- open http://server02 for Automationhub, and load `community/requirements.yml`

@bbaassssiiee
