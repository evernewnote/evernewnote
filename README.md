
# Evernewnote

A new evernote.

## About

### Features

* Create and edit rich text notes

* Organize notes in notebooks

### File structure

Directory structure description below:

```python
evernewnote/
    - config/
        - base.py                   # Stores most settings
        - local.py                  # Stores settings only for local dev
        - production.py             # Stores settings only used by production (e.g. Heroku)
    - urls.py                       # Global urls.py, in turn includes urls.py in apps

- apps/                    
    - accounts/            
        - models.py                 # Customized user class
        - urls.py                   # URLs for sign-up and log-in pages
        - views.py                  # Views for sign-up and log-in pages
        - forms.py                  # Form for editing user profile, sign-up
        - templates/                # Templates for user profile stuff
    - core/                
        - static/                   # Static files
        - templates/                # Core templates, including base templates
        - admin.py                  # Admin panel allowing for adding Notes and Notebooks
        - forms.py                  # forms for creating notes and notebooks
        - models.py                 # Note and Notebook models
        - context_processors.py     # Add data for the sidebars to every context object
        - urls.py                   # URLs for creating and editing notes
        - views.py                  # views for the sidebars, new notes and editing notes
- manage.py                         # Entry point
- Pipfile                           # Development requirements
```


## Future features

### Near future
* New notebook without using admin panel
* File upload
* Note tagging
* Search
* Autosave on change
* More and better tests
* Sort notes via drop down menu
* Adding notes to shortcut menu
* Add print to pdf
* more metadata in notes
* Allow users to change profile
* Set a default notebook 

### Goals
* Implement Operational Transform
    * Wrap changes in OT delta objects
    * Write or use library to manage changes according to the OT algorithm
        * https://github.com/sachinrekhi/richtextpy
        * https://svn.apache.org/repos/asf/incubator/wave/whitepapers/operational-transform/operational-transform.html
        * https://en.wikipedia.org/wiki/Operational_transformation
    * Set up a server that implements the OT protocol

