Installation
=========================

Cloud-based platforms like Google COLAB or others are very useful for
teaching and demonstration purposes, because the effort to set up a
working environment is minimal.

Nevertheless, they always require an internet connection and in many
cases a login step. Also, some of them are not entirely Open Source.

Therefore, in this section we briefly describe one of the possible
approaches that can be used to install some tools useful for
developing with Python.

Actually, there are many possibilities to install it, and many systems
come with Python already installed. Installing all the required
libraries can be time consuming. To speed up the installation, there
are some "bundle" distributions that are "self contained" and contain
the main scientific/graphical packages. Hereinafter we provide some
details about `Anaconda` and `Miniconda`.

.. note:: We suggest to install the `Miniconda` package. However, if
    you prefer, please feel free to opt for other installation
    options. For example, the `Mamba` package manager seems to be a
    valid and faster alternative to `Conda` and `Miniconda`. To
    install it, you can follow the `link for the Mamba installation
    <https://mamba.readthedocs.io/en/latest/installation/mamba-installation.html>`_

Miniconda
***************

Miniconda is a subset of Anaconda project that contains only a reduced
number of packages pre-installed.  To install it, download the version
corresponding to your system at
`https://docs.conda.io/en/latest/miniconda.html
<https://docs.conda.io/en/latest/miniconda.html>`_. Hereinafter we
describe the installation procedure for `MS Windows`, but the
procedure should be similar also for other OSs.

Download the right file and then execute it. Follow the installation
prompt with the default options, that should be OK in most of the
cases.

After the installation, you should be able to find, among the
applications, something like "Anaconda prompt" or similar - open it.

There are some preliminary steps that are useful to set-up your Python
environment. These should be valid for all the OSs.
It is suggested to:

1) Check if on the right, at the beginning of the text line on your
   prompt, there is the string `(base)`. In that case, you should
   type::
     
     conda deactivate

   If when you open the "Anaconda prompt" there is no `(base)` text on
   the left side of your prompt, this step is not
   required. Nevertheless, running it should not create any problem to
   your set-up.
     
2) Miniconda creates by default a *virtual environment* called "base".
   Here I suggest to create a new virtual environment related to the
   course. For example, you can name it like the acronym of this
   course (here the acronym `pygreen` is used, but of course feel free to
   use any other name). Write on the prompt::
     
     conda create --name pygreen

   In this case we created the "virtual environment" ``pygreen``.

3) Activate the new environment::
     
     conda activate pygreen

   Now you should see on the left, at the beginning of your prompt
   line, the string ``(pygreen)``.
     
4) Install the required packages::
     
     conda install numpy scipy matplotlib spyder
     
   (Reply `y` or simply hit `<Enter>` to the installation requests. In
   general, the option between square brackets `[ ]` is the one
   selected by default if you only hit `<Enter>`. Be patient.)  These
   are the main packages that will be used during the course, but
   some other will be required and installed when needed.
   
5) Now you are ready to launch spyder, one of the available Integrated
   development environment (IDE) that you can use to develop with
   Python. From the prompt, simply write ``spyder`` and hit
   `<Enter>`. The latest versions of spyder should already be run in
   "background". Otherwise, if spyder does not run automatically in
   "background", you can use ``start /b spyder`` in MS Windows or
   ``spyder &`` in macOS or Linux.

Anaconda
***********************

.. warning:: Use this option only if you have a lot of free space on
	  your computer (it requires at least 1 Gigabyte of space) and
	  your computer is relatively recent. If you need a more
	  minimalist installation, please have a look at the
	  `Miniconda <Miniconda_>`_ option.

One of the most common pre-packed container of Python utilities and
libraries is `Anaconda <https://www.anaconda.com/>`_.

To install Anaconda, do the following: download from `this link
<https://www.anaconda.com/download/>`_ the distribution suitable for
your OS. I suggest you to download version 3.X (at the time of this
writing, the default version is **Python 3.11**).  Once downloaded,
follow the instructions step-by-step. If you do not have any other
Python version installed on your system, then you can keep the default
settings.

To see if the installation was OK:

On Linux:
    Open the shell, then write ``spyder`` (or in some cases
    ``spyder3``) and hit `<enter>`.

On Windows:
    From the `start` menu you should see all the installed
    packages. Launch ``Spyder``.

On Mac OS X:
    You can do like in Linux. Alternatively, double-click on the file
    `Launcher.app` stored in your home directory into the
    sub-directory `anaconda`, and Launch `spyder-app`.

In all the cases, after some time the working environment `spyder`
should appear.

   


Linux "system" packages
**********************************

.. note:: Use this option only if you are already quite familiar with
   Python and Linux. Otherwise, please consider installing using the
   `Miniconda <Miniconda_>`_ approach.

On Ubuntu you can use the package manager to install `spyder`,
`python3-numpy`, `python3-scipy`, `python3-matplotlib` and
`python3-pandas`. The procedure should be similar for other
distributions. Please also note that the use of a virtual environment
is strongly suggested.


