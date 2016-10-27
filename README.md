# scaffold

*Scaffold* (a.k.a. *scf*) is an opinionated bootstrap script for C++ projects.

It does not claim that its way is the "one true way" of doing things; however, it does make 
strong choices in project structure and tooling, and leaves little to be configured. 

*This is intentional*. The idea is that there are many wrong ways of doing things, 
and *scaffold* wants to provide just one good way. Furthermore, the opinionated 
choices it makes are the some of the most widespread practices currently.

## Why would I want to use scaffold?

It helps you with the menial parts of setting up a project and minimizes errors.

## How to use scaffold?

Create a directory that is named after the project you want to create, change into it and run `scf init`.

```
$ mkdir myproject && cd myproject
$ scf init
```

This will do the following:

  * Initialize a git repository
  * Create the following directories
    * `doc` - documentation
    * `src` - source files
    * `include` - header files
    * `env` - working directory (for debugging)
  * Create the following files
    * `.gitignore`
    * `.editorconfig`
    * `CMakeLists.txt`
    * `doc/mkdocs.yml`
    * `doc/index.md`
    * `include/version.h.in`
    * `README.md`
    
The files created will have a reasonable default content that can be used as a starting point for your project.
