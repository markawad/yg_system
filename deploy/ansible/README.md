# ansible_deploy

An ansible playbook that deploys a django application to a specific unix server and would configure and run nginx.

## Requirements
-  Ansible
-  A database Connection (To be added in your settings.py)
-  Linux Server
-  Valid ssh key configuration to server

## Steps

There are a couple of required things needed in order for this playbook to fit your needs.

- Add your settings.py file to templates/settings.py.j2.
- Replace the needed set of variables in settings.py.j2 with {{app.*}}.
- Add your application zip on the first level of the application directory.
- Reflect the changes on vars.yml to be able to read your newly added variables.
- Open inventory/hosts.yml and add your host(s) information where the app will be deployed.

## Build
```
ansible-playbook main.yml -i inventory/
```

## Build Procedure

The playbook would create the necessary directory structure for your django app, then it will scp the application zip to your host(s). It will replace the variables of settings.py.j2 with the vars in vars.yml and copy it to your remote settings.py location.

After this process has been done successfully, It will setup nginx and gunicorn to host your webserver according to the templates and the specified {{app.remote.site}}.

`Note:` The playbook is idempotent. Hence running it multiple times would be possible and keep the desired result.
