!["Gimel Studio banner"](/assets/banner/banner.png "Gimel Studio")

Gimel Studio
============

[![GitHub license](https://img.shields.io/github/license/GimelStudio/GimelStudio?color=light-green)](https://github.com/GimelStudio/GimelStudio/blob/master/LICENSE)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/GimelStudio/GimelStudio.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/GimelStudio/GimelStudio/context:python)

Gimel Studio is a non-destructive, node-based 2D image graphics editor written in Python, focused on **simplicity, speed, elegance and usability**.


# Vision

The main goal is to expand on and greatly improve upon the concepts from the [original version](https://github.com/Correct-Syntax/Gimel-Studio) of Gimel Studio to create a serious (yet fun!) 2D graphics editor. 

This includes a re-designed UI (highly inspired by Blender and Sketch), improved file-type support, node-graph and overall workflow for image editing. Nodes can be used to composite, create/add new effects and/or composite raster and vector graphics on-demand. Helpful gizmos in the interactive viewport can be used to do various editing tasks and speed up the workflow. Preset node graph templates can be created, used and re-used to save time setting up common node-setups. Custom nodes can be scripted with the built-in Python API for maximum flexibility. Integrations with other softwares like Blender are planned.

With a fully non-destructive workflow that uses both GPU and CPU processing while being seamlessly cross-platform on Windows, Linux and MacOs (for 64-bit systems), Gimel Studio aims to be a simple, yet powerful 2d graphics editing tool for beginners and pros alike.

**Visit our new home landing-page [here](https://gimelstudio.github.io) for some more detailed information on the project goals, vision, etc**


# About the Next Generation of Gimel Studio

**The original (more stable) version of Gimel Studio is available [here](https://github.com/Correct-Syntax/Gimel-Studio).**

This repository tracks the *next step* of Gimel Studio (the v0.6.x series) to become a truly usable and serious node-based, non-destructive image editor. It is currently in *initial development stage* and things will probably change (a lot) from what is currently here.


# Discord & Gitter

You're welcome to join us in planning/development for the next step of Gimel Studio!

If you'd like to join development or have questions, comments or ideas you can join the Gimel Studio [Discord](https://discord.gg/RqwbDrVDpK) or [Gitter](https://gitter.im/Gimel-Studio/community). These are places where you can chat with the developers and get the latest development updates.


# WIP Mockup

Here is a **WIP mockup** of the redesigned UI:

!["Gimel Studio mockup"](https://i.ibb.co/SPKdJxg/Updated-UI-Mockup.png "Gimel Studio")


# Roadmap Goals

For now, we're trying to keep the roadmap limited to realistic goals, keeping fun (of course!) and on-par with the amount of developers/contributors we have. *(Hint: we could possibly do more if you contribute.)*

**Visit our new home landing-page [here](https://gimelstudio.github.io) for some more detailed information on the project goals, vision, etc**


# Immediate Tasks

Take a look at the [Github Issues](https://github.com/GimelStudio/GimelStudio/issues) for some immediate and future tasks. PRs are welcome! :)


# Running the WIP code

At this early stage of development, the code is very WIP and likely to change a lot. Many things are not implemented, buggy and/or roughly implemented.

However, if you'd like to see the latest updates to the GUI and backend, you can do so by following the steps below:

1. ``pip install -r requirements.txt``
2. Get the OIIO (OpenImageIO) pre-built python wheel (Windows only) [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#openimageio) and install it.
2. ``python src/main.py``

Please note that the renderer, which relies on OIIO will be **disabled if OIIO is not found**. For platforms other than Windows, OIIO will need to be [built from source](https://github.com/OpenImageIO/oiio/blob/master/INSTALL.md#building-from-source) since pre-built wheels are not yet available. See [this issue](https://github.com/GimelStudio/GimelStudio/issues/1).


# Tech Stack

[Python](https://python.org) - We can effectively use Python's strong suits (ease-of-use, portability, multitude of packages, large community, etc) and get the performance required by relying on lower-level and performant external libraries to do the heavy lifting (where implementing something in Python would be a bottleneck). This should also lower the bar on contributing to Gimel Studio and thus (hopefully) allow for a greater contributor base.

We also plan to use **GLSL and/or it's variants in addition to Python** for image-editing, as applicable, via [ModernGL](https://github.com/moderngl/moderngl), [glnext](https://github.com/cprogrammer1994/glnext) or another graphics rendering API (suggestions welcome!). **(This is still undecided)**

[Numpy](https://numpy.org/) - Numpy will be the "data-exchange" format, the core image format used for the backend of Gimel Studio. It will be used as "glue" to combine OIIO, GMIC, etc.

[OpenImageIO](https://openimageio.readthedocs.io/en/release-2.2.8.0/) - OIIO will be used for image IO and (possibly) some image editing. OpenImageIO (OIIO) is a library for reading, writing, and processing images in a wide variety of file formats, using a format-agnostic API. It is used in professional, large-scale visual effects and feature film animation, and it is used ubiquitously by large VFX studios, as well as incorporated into many commercial products.

[Cario](https://pycairo.readthedocs.io/en/latest/) - Cairo is a 2D graphics library with support for multiple output devices, including SVG, etc. We will use either cairo or [Skia graphics engine](https://skia.org/) for vector graphics support.

[G'MIC](https://gmic.eu/) - For additional image effects and filters (CPU-based). *Mainly need to wait for the [GMIC python bindings](https://github.com/myselfhimself/gmic-py) to support Windows and MacOs before implementing this into Gimel Studio, but this probably won't be implemented until after the core is stable anyway.*

[wxPython](https://wxpython.org) -  Will be used as the **primary GUI front-end** as it's a powerful, native, cross-platform GUI toolkit based on wxWidgets. For good examples of wxpython used as a toolkit for graphics applications see [sK1 vector graphics editor](https://sk1project.net/) and [ImagePy](https://github.com/Image-Py).

A greatly improved nodegraph for Gimel Studio is currently in development via the [GS Nodegraph](https://github.com/GimelStudio/gsnodegraph) library.

Modern, style-able widgets for Gimel Studio are currently in development via the [GS WidgetKit](https://github.com/GimelStudio/gswidgetkit) library.

**API Scripting Language:** Python, of course. :)