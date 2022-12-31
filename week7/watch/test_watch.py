from watch import parse


def test_full_html():
    assert (
        parse(
            """<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
        )
        == "https://youtu.be/xvFZjo5PgG0"
    )
    assert (
        parse(
            """<iframe width="560" height="315" src="https://www.youtube.com/embed/bnJ3XQmmaz8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
        )
        == "https://youtu.be/bnJ3XQmmaz8"
    )
    assert (
        parse(
            """<iframe width="560" height="315" src="https://www.youtube.com/embed/0PakoE1eBps" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""
        )
        == "https://youtu.be/0PakoE1eBps"
    )


def test_shorten_html():
    assert (
        parse("""<iframe src="https://www.youtube.com/embed/X2mOfqeAH7c"></iframe>""")
        == "https://youtu.be/X2mOfqeAH7c"
    )
    assert (
        parse("""<iframe src="http://www.youtube.com/embed/Vwo1miUjDSc"></iframe>""")
        == "https://youtu.be/Vwo1miUjDSc"
    )
    assert (
        parse("""<iframe src="https://www.youtube.com/embed/8PhdfcX9tG0"></iframe>""")
        == "https://youtu.be/8PhdfcX9tG0"
    )


def test_no_youtube_link():
    assert (
        parse(
            """<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>"""
        )
        == None
    )
    assert (
        parse(
            """<iframe width="560" height="315" src="https://archlinux.org/"></iframe>"""
        )
        == None
    )
    assert (
        parse("""<iframe width="560" height="315" src="https://github.com"></iframe>""")
        == None
    )


def test_no_html():
    assert parse("""https://youtube.com/embed/xvFZjo5PgG0""") == None
    assert parse("""https://youtube.com/embed/zuqBRN5SJZ8""") == None
    assert parse("""https://youtube.com/embed/o8NPllzkFhE""") == None
