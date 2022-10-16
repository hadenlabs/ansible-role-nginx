<!-- Space: Projects -->
<!-- Parent: AnsibleRoleNginx -->
<!-- Title: Examples AnsibleRoleNginx -->
<!-- Label: Examples -->
<!-- Include: ./../disclaimer.md -->
<!-- Include: ac:toc -->

## packages

To run this playbook with default settings, for install package like this:

generate file `requirements.yml`

```yaml
- name: hadenlabs.ansible-role-nginx
  src: git+https://github.com/hadenlabs/ansible-role-nginx
  version: /main
```

```yaml
- hosts: all
  roles:
    - role: hadenlabs.ansible-role-nginx
      become: true
      vars:
        ansible-role-nginx_owner: ubuntu
```
