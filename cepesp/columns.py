CANDIDATOS = [
    "ANO_ELEICAO",
    "NUM_TURNO",
    "DESCRICAO_ELEICAO",
    "SIGLA_UF",
    "SIGLA_UE",
    "DESCRICAO_UE",
    "CODIGO_CARGO",
    "DESCRICAO_CARGO",
    "NOME_CANDIDATO",
    "SEQUENCIAL_CANDIDATO",
    "NUMERO_CANDIDATO",
    "CPF_CANDIDATO",
    "NOME_URNA_CANDIDATO",
    "COD_SITUACAO_CANDIDATURA",
    "DES_SITUACAO_CANDIDATURA",
    "NUMERO_PARTIDO",
    "SIGLA_PARTIDO",
    "NOME_PARTIDO",
    "CODIGO_LEGENDA",
    "SIGLA_LEGENDA",
    "COMPOSICAO_LEGENDA",
    "NOME_COLIGACAO",
    "CODIGO_OCUPACAO",
    "DESCRICAO_OCUPACAO",
    "DATA_NASCIMENTO",
    "NUM_TITULO_ELEITORAL_CANDIDATO",
    "IDADE_DATA_ELEICAO",
    "CODIGO_SEXO",
    "DESCRICAO_SEXO",
    "COD_GRAU_INSTRUCAO",
    "DESCRICAO_GRAU_INSTRUCAO",
    "CODIGO_ESTADO_CIVIL",
    "DESCRICAO_ESTADO_CIVIL",
    "CODIGO_COR_RACA",
    "DESCRICAO_COR_RACA",
    "CODIGO_NACIONALIDADE",
    "DESCRICAO_NACIONALIDADE",
    "SIGLA_UF_NASCIMENTO",
    "CODIGO_MUNICIPIO_NASCIMENTO",
    "NOME_MUNICIPIO_NASCIMENTO",
    "DESPESA_MAX_CAMPANHA",
    "COD_SIT_TOT_TURNO",
    "DESC_SIT_TOT_TURNO",
    "EMAIL_CANDIDATO"
]

LEGENDAS = [
    "ANO_ELEICAO",
    "CODIGO_CARGO",
    "COMPOSICAO_COLIGACAO",
    "DATA_GERACAO",
    "DESCRICAO_CARGO",
    "DESCRICAO_ELEICAO",
    "DESCRICAO_UE",
    "HORA_GERACAO",
    "NOME_COLIGACAO",
    "NOME_PARTIDO",
    "NUMERO_PARTIDO",
    "NUM_TURNO",
    "SEQUENCIA_COLIGACAO",
    "SIGLA_COLIGACAO",
    "SIGLA_PARTIDO",
    "SIGLA_UE",
    "SIGLA_UF",
    "TIPO_LEGENDA"
]

VOTOS = {

    # BR
    0: [
        "ANO_ELEICAO",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ],

    # MACRO
    1: [
        "ANO_ELEICAO",
        "CODIGO_MACRO",
        "NOME_MACRO",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ],

    # UF
    2: [
        "ANO_ELEICAO",
        "UF",
        "NOME_UF",
        "CODIGO_MACRO",
        "NOME_MACRO",
        "SIGLA_UE",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ],

    # MESO
    4: [
        "ANO_ELEICAO",
        "CODIGO_MESO",
        "NOME_MESO",
        "UF",
        "NOME_UF",
        "CODIGO_MACRO",
        "NOME_MACRO",
        "SIGLA_UE",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ],

    # MICRO
    5: [
        "ANO_ELEICAO",
        "CODIGO_MICRO",
        "NOME_MICRO",
        "CODIGO_MESO",
        "NOME_MESO",
        "UF",
        "NOME_UF",
        "CODIGO_MACRO",
        "NOME_MACRO",
        "SIGLA_UE",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ],

    # MUNICIPIO
    6: [
        "ANO_ELEICAO",
        "COD_MUN_TSE",
        "COD_MUN_IBGE",
        "NOME_MUNICIPIO",
        "CODIGO_MICRO",
        "NOME_MICRO",
        "CODIGO_MESO",
        "NOME_MESO",
        "UF",
        "NOME_UF",
        "CODIGO_MACRO",
        "NOME_MACRO",
        "SIGLA_UE",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ],

    # MUNZONA
    7: [
        "ANO_ELEICAO",
        "NUM_ZONA",
        "COD_MUN_TSE",
        "COD_MUN_IBGE",
        "NOME_MUNICIPIO",
        "CODIGO_MICRO",
        "NOME_MICRO",
        "CODIGO_MESO",
        "NOME_MESO",
        "UF",
        "NOME_UF",
        "CODIGO_MACRO",
        "NOME_MACRO",
        "SIGLA_UE",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ],

    # ZONA
    8: [
        "ANO_ELEICAO",
        "NUM_ZONA",
        "CODIGO_MICRO",
        "NOME_MICRO",
        "CODIGO_MESO",
        "NOME_MESO",
        "UF",
        "NOME_UF",
        "CODIGO_MACRO",
        "NOME_MACRO",
        "SIGLA_UE",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ],

    # VOTACAO SECAO
    9: [
        "ANO_ELEICAO",
        "NUM_SECAO",
        "NUM_ZONA",
        "CODIGO_MICRO",
        "NOME_MICRO",
        "CODIGO_MESO",
        "NOME_MESO",
        "UF",
        "NOME_UF",
        "CODIGO_MACRO",
        "NOME_MACRO",
        "COD_MUN_TSE",
        "COD_MUN_IBGE",
        "NOME_MUNICIPIO",
        "NUM_TURNO",
        "DESCRICAO_ELEICAO",
        "SIGLA_UE",
        "CODIGO_CARGO",
        "DESCRICAO_CARGO",
        "NUMERO_CANDIDATO",
        "QTDE_VOTOS"
    ]

}
