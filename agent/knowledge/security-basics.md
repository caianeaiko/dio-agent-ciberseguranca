
# Fundamentos de Segurança da Informação

## Objetivo

Fornecer ao DIO Agent conhecimentos fundamentais sobre segurança da informação para apoiar análises de vulnerabilidades, avaliações de risco e recomendações defensivas.

## 1. Conceitos fundamentais

### Vulnerabilidade

Uma vulnerabilidade é uma fraqueza em um sistema, aplicação, configuração ou processo que pode ser explorada por uma ameaça.

Exemplo: uma aplicação que utiliza concatenação de entradas do usuário em consultas SQL.

### Ameaça

Uma ameaça é qualquer evento, agente ou circunstância com potencial de causar danos a um sistema ou organização.

Exemplo: um atacante que tenta explorar uma falha de autenticação.

### Risco

Risco é a possibilidade de uma ameaça explorar uma vulnerabilidade e causar consequências negativas.

A avaliação deve considerar a probabilidade de ocorrência e o impacto potencial.

## 2. Tríade CIA

A segurança da informação é baseada em três princípios:

### Confidencialidade

Garantir que informações sejam acessadas apenas por pessoas autorizadas.

Exemplo: proteger dados pessoais e credenciais.

### Integridade

Garantir que informações não sejam alteradas indevidamente.

Exemplo: impedir modificações não autorizadas em registros de um banco de dados.

### Disponibilidade

Garantir que sistemas e informações estejam acessíveis quando necessários.

Exemplo: manter serviços funcionando e reduzir interrupções.

## 3. Avaliação de riscos

A análise deve considerar:

- Impacto: consequências de uma possível exploração.
- Probabilidade: possibilidade de a exploração ocorrer.
- Severidade: prioridade da vulnerabilidade considerando o contexto.

Classificação sugerida:

| Nível | Descrição |
| --- | --- |
| Baixo | Consequências limitadas e facilmente controláveis. |
| Médio | Impacto moderado, exigindo correção planejada. |
| Alto | Possibilidade de comprometimento significativo. |
| Crítico | Potencial de consequências graves e necessidade de resposta urgente. |

A classificação deve ser justificada e não deve ser considerada definitiva sem informações suficientes.

## 4. Vulnerabilidades comuns

### SQL Injection — CWE-89

Ocorre quando entradas não confiáveis são incorporadas indevidamente a comandos SQL.

Mitigação: utilizar consultas parametrizadas e aplicar o princípio do menor privilégio.

### Cross-Site Scripting (XSS)

Ocorre quando conteúdo não confiável é interpretado como código executável pelo navegador.

Mitigação: codificação de saída adequada ao contexto, sanitização quando necessária e políticas de segurança complementares.

### Autenticação insegura

Problemas em mecanismos de login e gerenciamento de credenciais podem permitir acesso indevido.

Mitigação: armazenamento seguro de senhas, limitação de tentativas e autenticação multifator quando apropriada.

### Configurações inseguras

Serviços expostos, permissões excessivas e configurações inadequadas podem aumentar a superfície de ataque.

Mitigação: revisão de configurações, atualização de sistemas e redução de serviços desnecessários.

## 5. Referências de segurança

### CWE

O Common Weakness Enumeration é um catálogo de tipos de fraquezas em software e hardware.

### CVE

O Common Vulnerabilities and Exposures identifica vulnerabilidades divulgadas publicamente por meio de identificadores padronizados.

### MITRE ATT&CK

É uma base de conhecimento sobre táticas e técnicas utilizadas por adversários.

Uma vulnerabilidade CWE não corresponde automaticamente a uma técnica ATT&CK. A associação depende do cenário de exploração.

## 6. Boas práticas

- Aplicar o princípio do menor privilégio.
- Manter sistemas e dependências atualizados.
- Utilizar consultas parametrizadas.
- Proteger credenciais e informações sensíveis.
- Implementar autenticação e autorização adequadas.
- Monitorar eventos relevantes de segurança.
- Realizar backups e testar procedimentos de recuperação.
- Validar correções em ambientes controlados.
- Documentar vulnerabilidades e medidas de mitigação.

## 7. Uso ético

Toda análise deve ocorrer em sistemas próprios ou mediante autorização explícita.

O agente deve priorizar orientações defensivas, solicitar contexto e evitar ações que possam causar danos.

## 8. Aplicação no DIO Agent

Este conhecimento complementa a skill `vulnerability-analysis`.

O agente deve utilizar esses conceitos para explicar vulnerabilidades, avaliar riscos e orientar correções de maneira educativa e estruturada.
