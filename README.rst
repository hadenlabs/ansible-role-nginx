Ansible Role Nginx
==================

|Build Status| |Ansible Galaxy| |GitHub issues| |Percentage of issues still open| |GitHub license|

:Version: 0.0.0
:Web: https://github.com/equipindustry/ansible-role-nginx
:Download: http://github.com/equipindustry/ansible-role-nginx
:Source: http://github.com/equipindustry/ansible-role-nginx
:Keywords: ansible-role-nginx

.. contents:: Table of Contents:
    :local:

Ansible Galaxy role for `Nginx`_.

Requirements:
-------------

List of applications:

- `Python 3.6.4`_
- `Docker`_
- `Docker Compose`_

Install
-------

Install it with the following command:

.. code-block:: bash

    $ ansible-galaxy install equipindustry.nginx

Role Variables
--------------

The default role variables in ``defaults/main.yml`` are:

.. code-block:: yaml

    # defaults file for nginx
    nginx_keepalive_timeout: "65"
    nginx_keepalive_requests: "1000"

    nginx_client_max_body_size: "64m"
    nginx_client_body_timeout: "3m"
    nginx_client_header_timeout: "3m"

    nginx_server_names_hash_bucket_size: "64"


Dependencies
------------

None

Example Playbook
----------------

See the `examples <./examples/>`__ directory.

To run this playbook with default settings, create a basic playbook like
this:

.. code:: yaml

        - hosts: servers
          roles:
            - equipindustry.nginx

License
-------

The code in this repository is licensed under the Apache unless
otherwise noted.

Please see LICENSE_ for details.

Changelog
---------

Please see `CHANGELOG`_ for more information what
has changed recently.

Contributing
------------

Please see `CONTRIBUTING`_ for details.

Credits
-------

-  `author`_
-  `contributors`_

Made with :heart: :coffee: and :pizza: by `author`_ and `company`_.

.. Badges:

.. |Build Status| image:: https://travis-ci.org/equipindustry/ansible-role-nginx.svg
   :target: https://travis-ci.org/equipindustry/ansible-role-nginx
.. |Ansible Galaxy| image:: https://img.shields.io/badge/galaxy-equipindustry.python-blue.svg
   :target: https://galaxy.ansible.com/equipindustry/ansible-role-nginx/
.. |GitHub issues| image:: https://img.shields.io/github/issues/equipindustry/ansible-role-nginx.svg
   :target: https://github.com/equipindustry/ansible-role-nginx/issues
.. |Average time to resolve an issue| image:: http://isitmaintained.com/badge/resolution/equipindustry/ansible-role-nginx.svg
   :target: http://isitmaintained.com/project/equipindustry/ansible-role-nginx
.. |GitHub license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
   :target: LICENSE

.. Links
.. _`changelog`: CHANGELOG.rst
.. _`contributors`: AUTHORS
.. _`contributing`: CONTRIBUTING.rst
.. _`LICENSE`: LICENSE

.. _`company`: https://github.com/equipindustry
.. _`author`: https://github.com/luismayta

.. dependences
.. _Nginx: https://www.nginx.com
.. _Python: https://www.python.org
.. _Python 3.6.4: https://www.python.org/downloads/release/python-364
.. _Docker: https://www.docker.com/
.. _Docker Compose: https://docs.docker.com/compose/
