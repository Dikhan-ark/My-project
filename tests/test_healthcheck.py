from app.healthcheck import check_env


def test_missing_env(monkeypatch):
    monkeypatch.setattr("app.healthcheck.load_dotenv", lambda: None)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.delenv("OPENAI_MODEL", raising=False)
    assert check_env() == ["OPENAI_API_KEY", "OPENAI_MODEL"]
