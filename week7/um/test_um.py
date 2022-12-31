from um import count


def test_um_in_sentences():
    assert count("That's it for, um, today") == 1
    assert count("Can I get, um, a kiss?") == 1
    assert count("I want, um, to ask you something. Um... I don't know how, um...") == 3
    assert count("This was, um, CS50! Um.. congratulations.") == 2


def test_um_as_sentence():
    assert count("Um... Hello!") == 1
    assert count("Let me think... Um... Oh, now I know!") == 1
    assert count("Um?! What did you say? Um... Yes.") == 2


def test_um_within_words():
    assert count("His documentation of the results was excellent") == 0
    assert count("Butkara stupa was monumentalized by the addition of Hellenistic") == 0
    assert (
        count("He produced very convincing argumentation in support of the proposal.")
        == 0
    )


def test_words_that_starts_with_um():
    assert count("I took his umbrella by mistake.") == 0
    assert count("A large deposit of umber is worked in the neighbourhood.") == 0
    assert (
        count(
            "I am sorry that he took such umbrage at our raising this issue and cast aspersions on our purpose."
        )
        == 0
    )
    assert (
        count(
            "His walls are not wainscoted, and there is about his house no umbrageous park nor verdant lawn."
        )
        == 0
    )


def test_fake_ums():
    assert count("Umm... I don't know Rick") == 0
    assert count("Uum, oh now I see!") == 0
    assert count("Ummm.. I feel hungry") == 0
