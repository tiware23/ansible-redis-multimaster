ansible-redis-cluster-multiserver
========

An Ansible role that installs and configures redis cluster server

Requirements
------------

An Enterprise Linux

Role Variables
--------------

Use estas variaveis para configurar o host de redis que será master e qual será o password usado.

```
redis_node01:
redis_node02:
redis_node03:
redis_node04:
redis_node05:
redis_node06:
redis_port: "6379"

# Redis with Authentication
redis_auth:
 - auth: false
   pass:

```

Dependencies
------------

RVM repo.


Example Playbook
----------------

```sh
- hosts: redis-server
  roles:
  - role: redis-cluster
```

Test Molecule
------------

Use o molecule para validar esta role.

## Dependencias

```
Ansible >= 2.4
Python 2.7
Python >= 3.6 with Ansible >= 2.4

$ pip install virtualenv
$ virtualenv --no-site-packages .venv
$ source .venv/bin/activate

$ pip install molecule docker
```

## Execução

```
$ molecule test
```

License
-------

Apache License 2.0

Author Information
------------------


[Thiago N Cavalcante]: https://www.linkedin.com/in/thiago-cavalcante-1a9906117
