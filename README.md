SISTEMA SISVENDA

ESTRUTURA
	- CLIENTE;
		NOME;
		FOTO;
		- DOCUMENTO;
			NUMERO;
			TIPO;
			EMISSAO;
			VENCIMENTO;
			ATIVO;
		- ENDERECO;
			CEP;
			TIPO;
			DESCRICAO;
			COMPLEMENTO;
			NUMERO;
			ATIVO;
		- EMAIL;
			DESCRICAO
			ATIVO;
		
	- FORNECEDOR;
		NOME;
		FOTO;
		- DOCUMENTO;
			NUMERO;
			TIPO;
			EMISSAO;
			VENCIMENTO;
			ATIVO;
		- ENDERECO;
			CEP;
			TIPO;
			DESCRICAO;
			COMPLEMENTO;
			NUMERO;
			ATIVO;
		- EMAIL;
			DESCRICAO
			ATIVO;
		- PRODUTO {LISTA DE PRODUTO DESSE FORNECEDOR};
	- UNIDADE;
		DESCRICAO;
		FATOR;
		
	- PRODUTO;
		FOTO;
		DESCRICAO;
		UNIDADE;
		ESTOQUE;
		
	- PEDIDO;
		- ITEM;
			PRODUTO;
			QUANTIDADE;
			VALOR;
	- VENDA;
		- ITEM;
			PRODUTO;
			QUANTIDADE;
			VALOR;
	- FINANCEIRO;
		ENTIDADE {C QUANDO CLIENTE F QUANDO FORNECEDOR};
		PARCELA;
		VALOR;
		DESCONTO;
		VALOR_PAGO

	- CONFIGURACAO
		QUANTIDADE_PARCELA;
	
