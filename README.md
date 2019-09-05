Mercurial hgweb container
=========================

Building
--------

Just use the standard Docker command line to build this:

    docker build -t anteru/hgweb .

Running
-------

The container expects one volume to be mounted with read permissions containing the Mercurial repositories. This volume must be mounted to `/var/hg/repos`. For example:

    docker run -it --rm -v /path/to/hg/repositories/:/var/hg/repos -p 8080:80 anteru/hgweb

The container will start into a bash console so you can explore the container. To exit, typing in `exit` is sufficient.
