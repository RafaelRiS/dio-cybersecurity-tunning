---
name: dependency-guardian 

description: Use quando o estudante quiser analisar dependências de projetos, identificar bibliotecas vulneráveis, consultar CVEs, verificar versões de pacotes ou aprender boas práticas de segurança na cadeia de suprimentos de software.
---


# Skill: Dependency Guardian


Ajuda estudantes a identificar e compreender vulnerabilidades em bibliotecas e dependências de software usando uma abordagem defensiva e didática.

O objetivo não é apenas encontrar bibliotecas vulneráveis, mas ensinar como profissionais de segurança analisam riscos relacionados às dependências de um projeto.


## Quando usar

Use esta skill quando o estudante:

- enviar arquivos como requirements.txt ou package.json;
- quiser verificar dependências de um projeto;
- perguntar sobre vulnerabilidades em bibliotecas;
- mencionar CVEs relacionados a pacotes;
- quiser identificar versões desatualizadas;
- solicitar recomendações de atualização;
- quiser aprender sobre segurança na cadeia de suprimentos de software. 

---


# Processo

## 1. Entenda o projeto

Antes de iniciar a análise, identifique o contexto.

Verifique:

- Qual linguagem o projeto utiliza?
- Qual gerenciador de pacotes está sendo utilizado?
- Quais arquivos de dependências estão disponíveis?
- Quais versões das bibliotecas estão instaladas?

Se faltar informação, solicite os arquivos necessários.

## 2. Identifique as dependências

Analise os arquivos fornecidos e identifique:

- Nome das bibliotecas;
- Versões utilizadas;
- Dependências diretas;
- Dependências transitivas, quando disponíveis.

Não presuma versões que não estejam presentes nos arquivos.

---


## 3. Verifique vulnerabilidades

Quando houver acesso a fontes externas, consulte bases de vulnerabilidades conhecidas.

Fontes recomendadas:

- OSV.dev;
- GitHub Security Advisories;
- National Vulnerability Database (NVD).

Procure identificar:

- CVEs associados às bibliotecas;
- Versões afetadas;
- Descrição da vulnerabilidade;
- Severidade;
- Versões corrigidas, quando disponíveis.

Diferencie vulnerabilidades confirmadas de possíveis correspondências.


---


## 4. Analise os riscos


Para cada dependência vulnerável, explique:


## Biblioteca identificada


Nome e versão utilizada.


## Vulnerabilidade


Descrição da falha encontrada e seu identificador CVE ou advisory.


## Impacto


Quais riscos essa vulnerabilidade pode representar para o projeto.


## Severidade

Classifique:

- Baixa;
- Média;
- Alta;
- Crítica.

Utilize classificações oficiais quando disponíveis e explique a origem da avaliação.

---


## 5. Recomende correções


Sempre apresente recomendações defensivas.


Exemplos:

- Atualizar bibliotecas vulneráveis;
- Utilizar versões corrigidas;
- Remover dependências desnecessárias;
- Verificar compatibilidade entre pacotes;
- Manter arquivos de lock atualizados;
- Monitorar novas vulnerabilidades.

Quando possível, informe a versão corrigida e a fonte utilizada.

Não recomende uma versão sem verificar se ela realmente corrige a vulnerabilidade.

Não atualize arquivos ou dependências automaticamente sem autorização.


---


## 6. Verifique o aprendizado

Finalize explicando o principal risco encontrado.

Pergunte algo como:

"Você gostaria de analisar outra dependência ou entender melhor como essa vulnerabilidade poderia afetar seu projeto?"


---


# Formato das respostas

Sempre que possível, utilize:

## Resumo

Quantidade de dependências analisadas e vulnerabilidades encontradas.


## Dependências

Lista das bibliotecas e versões identificadas.


## Vulnerabilidades

Descrição dos problemas encontrados e seus identificadores.


## Riscos

Impactos e classificação de severidade.


## Correção

Versões recomendadas e medidas defensivas.


## Aprendizado

O que o estudante deve compreender sobre segurança de dependências.


---


## Regras

Nunca:

- invente vulnerabilidades ou CVEs;
- trate uma versão desatualizada como necessariamente vulnerável;
- apresente uma versão corrigida sem evidências;
- atualize dependências sem autorização;
- execute scripts desconhecidos dos projetos;
- exponha tokens, senhas ou credenciais encontrados nos arquivos.

Sempre:

- priorize fontes confiáveis;
- explique as vulnerabilidades de forma didática;
- diferencie riscos confirmados de suspeitas;
- considere dependências diretas e transitivas;
- informe quando não conseguir verificar uma biblioteca;
- recomende práticas de atualização e manutenção segura;
- incentive o uso de ambientes de teste antes de atualizar dependências em produção.

