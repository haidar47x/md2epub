### md2epub

*md2epub* is a Sigil compatible script that can convert Markdown files to XHTML. The converted files can be imported inside Sigil.

### Usage

Clone the repository and install the `markdown` dependency. Put the markdown files inside the `src` directory and update the `sections.json` file to include the files that need to be converted. I've already provided an existing template that we can readily use.

Next, simply convert the files:

```bash
$ python md2epub
```

The built files will be located in the `build` directory.
