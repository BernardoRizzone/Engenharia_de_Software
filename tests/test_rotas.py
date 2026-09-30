def test_contracts_exige_login(client): 
    resp = client.get("/contracts")

    assert resp.status_code == 302
    assert "/login" in resp.headers["Location"]

def test_login_valido_abre_painel(client): 
    resp = client.post("/login", data={ 
        "username": "gestor", 
        "password": "Gestor@123"}, 
        follow_redirects=True) 
    assert resp.status_code == 200

def test_trocar_senha_com_senha_atual_errada(client):
    
    client.post('/login', data={
        'username': 'gestor', 
        'password': 'Gestor@123'
    }, follow_redirects=True)

    
    resp = client.post('/change-password', data={
        'current_password': 'SenhaIncorreta123',
        'new_password': 'NovaSenha@321',
        'confirm_password': 'NovaSenha@321' 
    }, follow_redirects=True)
    
    assert resp.status_code == 200
    assert 'Senha atual incorreta.'.encode() in resp.data

def test_logout_redireciona_corretamente(client):
    
    client.post('/login', data={
        'username': 'gestor', 
        'password': 'Gestor@123'
    }, follow_redirects=True)
    
    
    resp = client.post('/logout', follow_redirects=True)
    
    assert resp.status_code == 200

def test_exportar_relatorio_csv(client):
    
    client.post('/login', data={
        'username': 'gestor', 
        'password': 'Gestor@123'
    }, follow_redirects=True)
    
    
    resp = client.get('/reports/orders.csv')
    
    assert resp.status_code == 200
    assert 'Número'.encode() in resp.data