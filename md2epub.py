import markdown
import os
import json
import shutil

def section_xml(fname):
    with open(os.path.join("src", fname), "r", encoding="utf-8") as f:
        md = f.read()
        doc = markdown.markdown(md, extensions=["codehilite","tables","fenced_code","footnotes"], extension_configs={"codehilite":{"guess_lang":False}})
    xhtml = """<?xml version="1.0" encoding="utf-8"?>\n"""
    xhtml += """<!DOCTYPE html>\n"""
    xhtml += """<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en">\n"""
    xhtml += """<head>\n<meta http-equiv="default-style" content="text/html; charset=utf-8"/>\n"""
    xhtml += """<link href="../Styles/main.css" rel="stylesheet" type="text/css"/>\n"""
    xhtml += """</head>\n<body>\n"""
    xhtml += doc
    xhtml += """\n</body>\n</html>"""
    return xhtml

def write_section(content, fname, _index):
    fname = os.path.join("build", f"Section{_index:04d}.xhtml")
    with open(fname, "w", encoding="utf-8") as f:
        f.write(content)

if __name__ == "__main__":

    # I/O directories
    if os.path.exists("build"):
        shutil.rmtree("build")
    os.makedirs("build")

    # Parse section filenames
    with open(os.path.join("src", "sections.json"),"r") as f:
        sections = json.load(f)

    # Get XML for sections and write to files
    _index = 2
    fnames = [section for section in sections]
    for fname in fnames:
        xml = section_xml(fname)
        write_section(xml, fname.split('.')[0], _index)
        _index += 1

