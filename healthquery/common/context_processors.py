def site_section(request):
    """
    Return a ContextProcessor with the tokens from the URL as a list.

    Eg. Templates accessed at a URL '/projects/foo/' will have a
    RequestContext processor with ``site_section`` available and equal to
    ['projects', 'foo'].
    
    To access in templates, use something like:
    
    {% if site_section.0 == "projects" %}...
    """

    try:
        ret = request.path.split('/')
    except IndexError:
        ret = ''
    # Avoid empty last token if URL ends with /
    if ret[-1] == '':
        ret.pop()
    return { 'site_section': ret[1:] }