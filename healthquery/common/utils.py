import re

def normalize_query(query_string,
        findterms=re.compile(r'\'([^\']+)\'|"([^"]+)"|(\S+)').findall,
    normspace=re.compile(r'\s{2,}').sub):
    """
    Splits the query string in individual keywords, getting rid of unnecessary
    spaces and grouping quoted words together.
    Example:

    >>> normalize_query('  some random  words "with   quotes  " and   spaces')
    ['some', 'random', 'words', 'with quotes', 'and', 'spaces']

    """
    return list([normspace(' ', (t[0] or t[1] or t[2]).strip()) for t in
        findterms(query_string)])

def get_tags_from_query(query_string):
    query_words_list = normalize_query(query_string)
    tags_list = set([])
    query_len = len(query_words_list)
    for n, word in enumerate(query_words_list):
        tags_list.add(word)
        if n < query_len - 1:
            tags_list.add(" ".join([word, query_words_list[n+1]]))
        if n < query_len - 2:
            tags_list.add(" ".join([word, query_words_list[n+1],
                query_words_list[n+2]]))
    return list(tags_list)
