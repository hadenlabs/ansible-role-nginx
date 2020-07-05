Ansible Role Nginx
==================

Ansible Role Nginx

|Build Status| |GitHub issues| |GitHub license|

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

- `Pyenv`_
- `Docker`_

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

Quick Start
===========

- Fork this repository

Usage
-----

- Install dependences

.. code-block:: bash

  λ make setup

Support
-------

If you want to support this project, i only accept ``IOTA`` :p.

.. code-block:: bash

    Address: FTDCZELEMOQGL9MBWFZENJLFIZUBGMXLFVPRB9HTWYDYPTFKASJCEGJMSAXUWDQC9SJUDMZVIQKACQEEYPEUYLAMMD


Team
----

+---------------+
| |Luis Mayta|  |
+---------------+
| `Luis Mayta`_ |
+---------------+

License
-------

MIT

Changelog
---------

Please see `CHANGELOG`_ for more information what
has changed recently.

Contributing
------------

Contributions are welcome!

Review the `CONTRIBUTING`_ for details on how to:

* Submit issues
* Submit pull requests

Contact Info
------------

Feel free to contact me to discuss any issues, questions, or comments.

* `Email`_
* `Twitter`_
* `GitHub`_
* `LinkedIn`_
* `Website`_
* `PGP`_

|linkedin| |beacon| |made|

Made with :coffee: and :pizza: by `Luis Mayta`_ and `equipindustry`_.

.. Links
.. _`changelog`: CHANGELOG.rst
.. _`contributors`: docs/source/AUTHORS.rst
.. _`contributing`: docs/source/CONTRIBUTING.rst

.. _`equipindustry`: https://github.com/equipindustry
.. _`Luis Mayta`: https://github.com/luismayta


.. _`Github`: https://github.com/luismayta
.. _`Linkedin`: https://pe.linkedin.com/in/luismayta
.. _`Email`: slovacus@gmail.com
    :target: mailto:slovacus@gmail.com
.. _`Twitter`: https://twitter.com/slovacus
.. _`Website`: https://luismayta.github.io
.. _`PGP`: https://keybase.io/luismayta/pgp_keys.asc

.. |Build Status| image:: https://travis-ci.org/equipindustry/ansible-role-nginx.svg
   :target: https://travis-ci.org/equipindustry/ansible-role-nginx
.. |GitHub issues| image:: https://img.shields.io/github/issues/equipindustry/ansible-role-nginx.svg
   :target: https://github.com/equipindustry/ansible-role-nginx/issues
.. |GitHub license| image:: https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square
   :target: LICENSE

.. Team:
.. |Luis Mayta| image:: https://github.com/luismayta.png?size=100
   :target: https://github.com/luismayta

.. Footer:
.. |linkedin| image:: http://www.linkedin.com/img/webpromo/btn_liprofile_blue_80x15.png
   :target: https://pe.linkedin.com/in/luismayta
.. |beacon| image:: https://ga-beacon.appspot.com/UA-65019326-1/github.com/equipindustry/ansible-role-nginx/readme
   :target: https://github.com/equipindustry/ansible-role-nginx
.. |made| image:: https://img.shields.io/badge/Made%20with-Zsh-1f425f.svg
   :target: http://www.zsh.org

.. Dependences:

.. _Pyenv: https://github.com/pyenv/pyenv
.. _Docker: https://www.docker.com/
.. _Nginx: https://nginx.org/
