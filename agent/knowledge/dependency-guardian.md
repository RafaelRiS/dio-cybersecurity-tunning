# Fundamentos de Segurança de Dependências


## Dependências

Dependências são bibliotecas, pacotes ou componentes externos utilizados por um projeto para adicionar funcionalidades.


## Dependência Vulnerável

Uma dependência vulnerável é uma biblioteca que possui uma falha de segurança conhecida em determinada versão.


## CVE

CVE (Common Vulnerabilities and Exposures) é um identificador utilizado para catalogar vulnerabilidades de segurança conhecidas.


## Dependências Diretas

São bibliotecas adicionadas diretamente pelo desenvolvedor ao projeto.


## Dependências Transitivas

São bibliotecas instaladas automaticamente porque outras dependências precisam delas.


## Versões de Dependências

Cada biblioteca possui diferentes versões, que podem incluir correções, melhorias e novas funcionalidades.

Uma versão antiga não significa necessariamente que exista uma vulnerabilidade.


## Severidade

Representa o nível de gravidade de uma vulnerabilidade.

Classificações comuns:

- Baixa;
- Média;
- Alta;
- Crítica.


## Fontes de Vulnerabilidades

Bases utilizadas para consultar problemas de segurança conhecidos:

- OSV.dev;
- GitHub Security Advisories;
National Vulnerability Database (NVD).


## Boas práticas

- manter dependências atualizadas;
- utilizar arquivos de lock;
- verificar vulnerabilidades conhecidas;
- remover bibliotecas desnecessárias;
- utilizar versões corrigidas;
- monitorar dependências transitivas;
- verificar a compatibilidade antes de atualizar;
- consultar fontes confiáveis de segurança;
- revisar dependências periodicamente;
- testar atualizações antes de aplicá-las em produção.