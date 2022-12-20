# SDII
 Sistema de atendimento por senha eletronica

Projeto de Disciplina Sistemas Distribuídos

SISTEMA DE ATENDIMENTO POR SENHA ELETRÔNICA

1. Introdução
Um Sistema de Atendimento por Senha Eletrônica (SASE) consiste de uma solução de
software distribuído, o qual gera automaticamente senhas eletrônicas visando aumento de
qualidade no atendimento ao público, através o gerenciamento e aumento de eficiência de
filas de pessoas em áreas de atendimento.
Comumente, um SASE inclui os seguintes elementos básicos:
1.1 - Senha Eletrônica de Atendimento (SEA): identificação disponibilizada ao público
e utilizada para ordenar os atendimentos;
1.2 - Terminal de Senhas (TS): dispositivo utilizado pelo público para geração de
senhas;
1.3 - Terminal de Atendimento (TA): local onde serão atendidas as pessoas que
receberam uma senha, gerada previamente no TS;
1.4 - Terminal de Visualização (TV): dispositivo que mostrará, em tempo real, as
senhas e os respectivos TAs, em atendimento;
1.5 - Servidor (SRV): computador que guardará informações sobre as senhas geradas,
senhas que estão em atendimento ou aquelas que já foram atendidas.

2. Especificação
Este projeto é um exercício prático que tem como objetivo solidificar os conhecimentos
teóricos vistos em sala de aula baseando-se em uma vivência no desenvolvimento de
aplicações distribuídas.
O exercício consiste no projeto e implementação de um SASE, objetivando
estabelecer o fluxo de atendimento completo do sistema proposto.
2.1. Programação da solução
O SASE a ser desenvolvido deverá atender às seguintes especificações:
1) Incluir os módulos distribuídos: TS, TA, TV e SRV;
2) Ser Implementado em qualquer linguagem de programação;
3) Utilizar sockets para comunicação entre os módulos TS, TA, TV e SRV;
4) Os módulos devem:
1) TS:
(a) Gerar dois tipos de SEA: Normal (N) ou Prioritário (P);
(b) Gerar as SEAs em ordem crescente. Exs; N1, N2, N3, P1, P2, P3,... ;
(c) Enviar as SEAs geradas para o SRV;
2) TA:
(a) Solicitar uma SEA ao SRV;
(b) Receber, após solicitação, uma SEA do SRV;
(c) A SEA recebida deve ter sido gerada anteriormente no TS;
(d) Informar a SEA recebida;
3) TV:
(a) Receber uma SEA do servidor;
(b) A SEA recebida deve ter sido gerada anteriormente no TS;
(c) A SEA recebida deve ser a mesma solicitada e recebida por um TA;
(d) Informar a SEA recebida;
4) SRV:
(a) Registrar as SEAs geradas pelo TS;
(b) Informar o instante em que recebeu uma nova SEA do TS;
(c) Enviar as SEAs registradas aos TAs e TVs, quando um TA solicitar uma
nova SEA. Para cada duas SEAs do tipo N informadas, a próxima SEA
deverá ser obrigatoriamente do tipo P, se houver.
(d) Informar o instante em que enviou uma SEA para TA e TV.