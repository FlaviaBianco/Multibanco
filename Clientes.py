cliente = {    
    
    "1001": 
    {
        "titular": "João Silva",
        "pin": "1234",
        "saldo": 1000.00,
        "bloqueado": False,
        "iban": "PT500001000200030004",
        "tentativas": 0,
        "movimentos": [
            {
                "tipo": "Depósito",
                "valor": 200,
                "data": "2026-05-26 14:30",
                "destino": None,
                "descricao": "Depósito em numerário"
            },
            {
                "tipo": "Transferência",
                "valor": 100,
                "data": "2026-05-26 16:30",
                "destino": "PT500009999999999",
                "descricao": "Transferência bancária"
            }
        ]
    },

    "1002": {
        "titular": "Maria Costa",
        "pin": "4321",
        "saldo": 2500.00,
        "tentativas": 0,
        "iban": "PT500005555555555",
        "bloqueado": False,
        "movimentos": [
            {
            "tipo": "Levantamento",
            "valor": 50,
            "data": "2026-05-26 10:00",
            "destino": None,
            "descricao": "Levantamento ATM"
            }
        ]
    },

    "1003": { 
        "titular": "Pedro Santos",
        "pin": "5678",
        "saldo": 500.00,
        "tentativas": 0,        
        "iban": "PT500007777777777",
        "bloqueado": False,           
        "movimentos": []
    }
}