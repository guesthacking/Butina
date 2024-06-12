import json
import requests
from telethon import TelegramClient, events, Button


api_id = '28352385'
api_hash = '0d629a280257a429d72542b746f15154'
bot_token = '7395999838:AAE6y8W3pPcN6Ypae6ep_V_V60NC5mEENtw'


client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


def consultar_api(tipo, query):
    url = f'https://databit.online/api?token=0239cd36-829d-4635-a13d-9c238082b57a&type={tipo}&query={query}'
    response = requests.get(url)
    return response.json()


def formatar_resposta_cpf(dados):
    if dados["status"] != 200:
        return "Errei fui muleki, mano"

    dados_pessoais = dados.get("dadosBasicos", {})
    filiacao = dados.get("filiacao", {})
    emails = dados.get("emails", [{}])[0]
    telefones = dados.get("telefones", [{}])
    enderecos = dados.get("enderecos", [{}])[0]

    resposta = (
        "🔎 Consulta Realizada\n\n"
        "DADOS PESSOAIS:\n\n"
        f"CPF: {dados_pessoais.get('cpf', '')}\n"
        f"CNS: {dados_pessoais.get('cns', '')}\n"
        f"NOME: {dados_pessoais.get('nome', '')}\n"
        f"SEXO: {dados_pessoais.get('sexo', '')}\n"
        f"NASC: {dados_pessoais.get('nascimento', '').split()[0]}\n\n"
        "FILIAÇÃO:\n\n"
        f"MÃE: {filiacao.get('mae', '')}\n"
        f"PAI: {filiacao.get('pai', '')}\n\n"
        "CONTATO:\n\n"
        f"EMAIL: {emails.get('email', '')}\n\n"
        "TELEFONES:\n\n"
    )

    for telefone in telefones:
        resposta += f"{telefone.get('telefone', '')}\nwhatsapp: {telefone.get('whatsapp', 'null')}\n"

    resposta += (
        "\nENDEREÇO:\n\n"
        f"TIPO LOGRADOURO: {enderecos.get('tipoLogradouro', '')}\n"
        f"LOGRADOURO: {enderecos.get('logradouro', '')}\n"
        f"NÚMERO: {enderecos.get('logradouroNumero', '')}\n"
        f"COMPLEMENTO: {enderecos.get('complemento', '')}\n"
        f"BAIRRO: {enderecos.get('bairro', '')}\n"
        f"CIDADE: {enderecos.get('cidade', '')}\n"
        f"UF: {enderecos.get('uf', '')}\n"
        f"CEP: {enderecos.get('cep', '')}\n\n"
        f"Dev: @Webzin116\n"
        "Bot By: Squadblack"
    )
    return resposta


def formatar_resposta_nome(dados):
    if not dados:
        return "Já falei que errei, mano"

    dados_pessoais = dados[0]
    
    resposta = (
        "🔎 Consulta Realizada\n\n"
        f"NOME: {dados_pessoais.get('nome', '')}\n"
        f"CPF: {dados_pessoais.get('cpf', '')}\n"
        f"SEXO: {dados_pessoais.get('sexo', '')}\n"
        f"NASC: {dados_pessoais.get('data_nascimento', '')}\n"
        f"MÃE: {dados_pessoais.get('mae', '')}\n\n"
        f"Dev: @Webzin116\n"
        f"Bot By: Squadblack\n"
    )
    return resposta


def formatar_resposta_tel(dados):
    if not dados:
        return "Errei, mano"

    resposta = "🔎 Consulta Realizada\n\n"
    for item in dados:
        endereco = item.get('endereco', {})
        resposta += (
            f"CPF: {item.get('cpf', '')}\n"
            f"NOME: {item.get('nome', '')}\n\n"
            "ENDEREÇO:\n"
            f"TIPO: {endereco.get('tipo', '')}\n"
            f"LOGRADOURO: {endereco.get('logradouro', '')}\n"
            f"NÚMERO: {endereco.get('numero', '')}\n"
            f"BAIRRO: {endereco.get('bairro', '')}\n"
            f"CEP: {endereco.get('cep', '')}\n"
            f"CIDADE: {endereco.get('cidade', '')}\n"
            f"UF: {endereco.get('uf', '')}\n\n"
            f"Dev: @Webzin116\n"
            f"Bot By: Squadblack\n"
        )
    return resposta


def formatar_resposta_placa(dados):
    if dados.get("status") != 200:
        return "Errei mano."

    dados_veiculo = dados.get("dados", {})
    proprietario = dados_veiculo.get("proprietario", {})
    multas = dados_veiculo.get("multas", {})
    faturado = dados_veiculo.get("faturado", {})
    ano = dados_veiculo.get("ano", {})
    localidade = dados_veiculo.get("localidade", {})

    resposta = (
        "🔎 Consulta Realizada\n\n"
        "Dono:\n\n"
        f"NOME: {proprietario.get('nome', '')}\n"
        f"CPF: {proprietario.get('cpf', '')}\n\n"
        "INFORMAÇÕES:\n\n"
        f"CHASSI: {dados_veiculo.get('chassi', '')}\n"
        f"MOTOR: {dados_veiculo.get('motor', '')}\n"
        f"RENAVAM: {dados_veiculo.get('renavam', '')}\n"
        f"PLACA: {dados_veiculo.get('placa', '')}\n"
        f"COMBUSTÍVEL: {dados_veiculo.get('combustivel', '')}\n"
        f"POTÊNCIA: {dados_veiculo.get('potencia', '')}\n"
        f"NACIONALIDADE: {dados_veiculo.get('nacionalidade', '')}\n"
        f"MODELO: {dados_veiculo.get('modelo', '')}\n"
        f"COR: {dados_veiculo.get('cor', '')}\n"
        f"TIPO_VEIC: {dados_veiculo.get('tipo_veiculo', '')}\n"
        f"ESPECIE: {dados_veiculo.get('especie_veiculo', '')}\n\n"
        "MULTAS:\n\n"
        f"COMETIMENTO: {multas.get('comentimento', '')}\n"
        f"STATUS: {multas.get('status', '')}\n"
        f"VALOR: {multas.get('valor', '')}\n\n"
        "FATURADO:\n\n"
        f"FATURADO: {faturado.get('faturado', '')}\n"
        f"TIPO_PESSOA: {faturado.get('tipo_pessoa', '')}\n"
        f"UF: {faturado.get('uf', '')}\n\n"
        "FABRICAÇÃO: {ano.get('fabricacao', '')}\n"
        "MODELO: {ano.get('modelo', '')}\n\n"
        "Localidade:\n\n"
        f"MUNICÍPIO: {localidade.get('municipio', '')}\n"
        f"UF: {localidade.get('uf', '')}\n\n"
        f"Dev: @Webzin116"
        f"Bot By: Squadblack\n"
    )
    return resposta


@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    await event.respond(
        "Olá, sou o bot de consultas da Squadblack\n"
        "Meus modelos estão abaixo:\n\n"
        "/cpf\n"
        "/nome\n"
        "/tel\n"
        "/placa\n",
        buttons=[
            [Button.url("DataB1t", "https://t.me/datab1t")],
            [Button.url("Discord", "https://discord.gg/ShWU8k2E")]
        ]
    )


@client.on(events.NewMessage(pattern='/cpf'))
async def cpf_handler(event):
    # Verifica se a mensagem é de um usuário específico
    if event.is_private and event.sender_id not in [5762483448, 5925488179]:
        return
    # Verifica se a mensagem é de um grupo específico
    if event.is_group and event.chat_id != -1002020514840:
        return
    
    # Extrai o CPF da mensagem
    message_parts = event.message.text.split()
    if len(message_parts) != 2:
        await event.reply('⚠️ Use: /cpf <CPF>')
        return
    
    cpf = message_parts[1]
    
    # Consulta a API com o CPF fornecido
    try:
        result = consultar_api('cpf', cpf)
        # Formata a resposta da API como uma string
        result_str = formatar_resposta_cpf(result)
        await event.reply(result_str, buttons=[
            [Button.url("DataB1t", "https://t.me/datab1t")],
            [Button.url("Discord", "https://discord.gg/ShWU8k2E")]
        ])
    except Exception as e:
        await event.reply(f'Erro')

# Handler para o comando /nome
@client.on(events.NewMessage(pattern='/nome'))
async def nome_handler(event):
    # Verifica se a mensagem é de um usuário específico
    if event.is_private and event.sender_id not in [5762483448, 5925488179]:
        return
    # Verifica se a mensagem é de um grupo específico
    if event.is_group and event.chat_id != -1002020514840:
        return
    
    # Extrai o nome da mensagem
    message_parts = event.message.text.split(maxsplit=1)
    if len(message_parts) != 2:
        await event.reply('⚠️ Use: /nome <Nome>')
        return
    
    nome = message_parts[1]
    
    # Consulta a API com o nome fornecido
    try:
        result = consultar_api('nome', nome)
        # Formata a resposta da API como uma string
        result_str = formatar_resposta_nome(result)
        await event.reply(result_str, buttons=[
            [Button.url("DataB1t", "https://t.me/datab1t")],
            [Button.url("Discord", "https://discord.gg/ShWU8k2E")]
        ])
    except Exception as e:
        await event.reply(f'Erro')

# Handler para o comando /tel
@client.on(events.NewMessage(pattern='/tel'))
async def tel_handler(event):
    # Verifica se a mensagem é de um usuário específico
    if event.is_private and event.sender_id not in [5762483448, 5925488179]:
        return
    # Verifica se a mensagem é de um grupo específico
    if event.is_group and event.chat_id != -1002020514840:
        return
    
    # Extrai o telefone da mensagem
    message_parts = event.message.text.split()
    if len(message_parts) != 2:
        await event.reply('⚠️ Use: /tel <Telefone>')
        return
    
    tel = message_parts[1]
    
    # Consulta a API com o telefone fornecido
    try:
        result = consultar_api('telefone', tel)
        # Formata a resposta da API como uma string
        result_str = formatar_resposta_tel(result)
        await event.reply(result_str, buttons=[
            [Button.url("DataB1t", "https://t.me/datab1t")],
            [Button.url("Discord", "https://discord.gg/ShWU8k2E")]
        ])
    except Exception as e:
        await event.reply(f'Erro')

# Handler para o comando /placa
@client.on(events.NewMessage(pattern='/placa'))
async def placa_handler(event):
    # Verifica se a mensagem é de um usuário específico
    if event.is_private and event.sender_id not in [5762483448, 5925488179]:
        return
    # Verifica se a mensagem é de um grupo específico
    if event.is_group and event.chat_id != -1002020514840:
        return
    
    # Extrai a placa da mensagem
    message_parts = event.message.text.split()
    if len(message_parts) != 2:
        await event.reply('⚠️ Use: /placa <Placa>')
        return
    
    placa = message_parts[1]
    
    # Consulta a API com a placa fornecida
    try:
        result = consultar_api('placa', placa)
        # Formata a resposta da API como uma string
        result_str = formatar_resposta_placa(result)
        await event.reply(result_str, buttons=[
            [Button.url("DataB1t", "https://t.me/datab1t")],
            [Button.url("Discord", "https://discord.gg/ShWU8k2E")]
        ])
    except Exception as e:
        await event.reply(f'Erro ao consultar a placa: {e}')

# Inicie o cliente Telegram
async def main():
    await client.start(bot_token=bot_token)

# Execute o loop principal
with client:
    client.loop.run_until_complete(main())
    client.run_until_disconnected()
    
