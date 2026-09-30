from models import User

def test_senha_nao_fica_em_texto_puro():
    u = User(username="teste")
    u.set_password("Segredo@123")
    assert u.password_hash != "Segredo@123"
    assert u.check_password("Segredo@123")