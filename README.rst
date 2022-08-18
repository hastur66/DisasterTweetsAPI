============
DisaterTweetsAPI
============


.. image:: https://img.shields.io/pypi/v/apiblueprint.svg
        :target: https://pypi.python.org/pypi/apiblueprint

.. image:: https://img.shields.io/travis/hastur66/apiblueprint.svg
        :target: https://travis-ci.com/hastur66/apiblueprint

.. image:: https://readthedocs.org/projects/apiblueprint/badge/?version=latest
        :target: https://apiblueprint.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




ML API projects for fake disater tweet detection


* Free software: MIT license
* Documentation: https://apiblueprint.readthedocs.io.


Features
--------

* 
An API for fake disater tweet detection using machine learning.

Dataset used --> [Kaggle](https://www.kaggle.com/competitions/nlp-getting-started)


Deploy API -->
```
python app.py
```

User Requests example -->
```
curl -X GET http://127.0.0.1:5000/ -d query='UFO caused a landslide'
```

Credits
-------
[Kaggle](https://www.kaggle.com/competitions/nlp-getting-started)

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
