import lotto


def test_play_a_game(monkeypatch, capsys):
    type = "MEGABALL"
    no_tickets = 1
    receipt = "no"
    answers = iter([type, str(no_tickets), receipt])

    monkeypatch.setattr('builtins.input', lambda type: next(answers))
    lotto.main()

    captured = capsys.readouterr()

    assert "Number" in captured.out


def test_reads_config_file():
    config = lotto.load_contest()

    assert 'contests' in config
    assert 'name' in config['contests'][0]
    assert 'amount' in config['contests'][0]
    assert 'start' in config['contests'][0]
    assert 'end' in config['contests'][0]
    assert 'extra' in config['contests'][0]
    assert 'extra_start' in config['contests'][0]
    assert 'extra_end' in config['contests'][0]
