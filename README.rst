
DISCLAIMER - ABANDONED/UNMAINTAINED CODE / DO NOT USE
=======================================================
While this repository has been inactive for some time, this formal notice, issued on **December 10, 2024**, serves as the official declaration to clarify the situation. Consequently, this repository and all associated resources (including related projects, code, documentation, and distributed packages such as Docker images, PyPI packages, etc.) are now explicitly declared **unmaintained** and **abandoned**.

I would like to remind everyone that this project’s free license has always been based on the principle that the software is provided "AS-IS", without any warranty or expectation of liability or maintenance from the maintainer.
As such, it is used solely at the user's own risk, with no warranty or liability from the maintainer, including but not limited to any damages arising from its use.

Due to the enactment of the Cyber Resilience Act (EU Regulation 2024/2847), which significantly alters the regulatory framework, including penalties of up to €15M, combined with its demands for **unpaid** and **indefinite** liability, it has become untenable for me to continue maintaining all my Open Source Projects as a natural person.
The new regulations impose personal liability risks and create an unacceptable burden, regardless of my personal situation now or in the future, particularly when the work is done voluntarily and without compensation.

**No further technical support, updates (including security patches), or maintenance, of any kind, will be provided.**

These resources may remain online, but solely for public archiving, documentation, and educational purposes.

Users are strongly advised not to use these resources in any active or production-related projects, and to seek alternative solutions that comply with the new legal requirements (EU CRA).

**Using these resources outside of these contexts is strictly prohibited and is done at your own risk.**

This project has been transfered to Makina Corpus <freesoftware-corpus.com> ( https://makina-corpus.com ). This project and its associated resources, including published resources related to this project (e.g., from PyPI, Docker Hub, GitHub, etc.), may be removed starting **March 15, 2025**, especially if the CRA’s risks remain disproportionate.

GitLab Auth for Sentry
======================
v0.1.0

An SSO provider for Sentry which enables GitLab Login

Changes made for Gitlab 9.x
----------
Following configuration has been changed

.. code-block:: python

  # You can specify scope to "api" in Gitlab's OAuth Application page
  # If you failed to do that, set GITLAB_AUTH_SCOPE = "read_user"
  GITLAB_AUTH_SCOPE = "api"
  # If your gitlab does not support v4 api, set GITLAB_API_VERSION = 3
  GITLAB_API_VERSION = 4


Install
-------

::

    pip install sentry-auth-gitlab

Setup
-----

Create a new application under your GitLab.
Enter the **Callback URL** as the prefix to your Sentry installation:

::

    http(s?)://sentry.example.com/auth/sso/


Once done, grab your API keys and drop them in your ``sentry.conf.py:

.. code-block:: python

    GITLAB_APP_ID = "APP-ID"
    GITLAB_APP_SECRET = "APP-SECRET"
    GITLAB_BASE_DOMAIN = "git.example.com"


Optionally you may also specify the api version, scheme, and scope:

.. code-block:: python

    GITLAB_API_VERSION = 4
    GITLAB_AUTH_SCOPE = "api"
    GITLAB_HTTP_SCHEME = "https"


Notice
------

If your gitlab is deployed in a private network (probably).
You need to alter sentry's default ip black list to make oauth flow work.

Put following config in your **sentry.conf.py** and delete conflit ones

.. code-block:: python

    SENTRY_DISALLOWED_IPS = (
        '0.0.0.0/8',
        '10.0.0.0/8',
        '100.64.0.0/10',
        '127.0.0.0/8',
        '169.254.0.0/16',
        '172.16.0.0/12',
        '192.0.0.0/29',
        '192.0.2.0/24',
        '192.88.99.0/24',
        '192.168.0.0/16',
        '198.18.0.0/15',
        '198.51.100.0/24',
        '224.0.0.0/4',
        '240.0.0.0/4',
        '255.255.255.255/32'
    )
