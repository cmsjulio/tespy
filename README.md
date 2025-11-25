# tespy

Estou tentando adapter o modelo existente do Tespy (ttps://tespy.readthedocs.io/en/main/basics/gas_turbine.html) 
onde ele utiliza um modelo simples de ciclo Brayton com 1 compressor, 1 camara de combustão e 1 turbine, utilizando CH4 como combustivel. 

Meu modelo consiste em 1 compressor de baixa pressao (LPC), 1 compressor de Alta pressao (HPC), 1 camara de combustão, 
1 turbina de Alta pressao (HPT) e 1 turbina de baixa pressao (LPC), utlizando como combustivel C12H24. 

Apos isso, preciso calcular a Exergia/eficiencia exergetica dos componentes e do ciclo com base no modelo existente 
(https://tespy.readthedocs.io/en/main/tutorials/heat_pump_exergy.html).

O trabalho gerado na HPT sera fornecido sem perdas ao HPC, assim como o trabalho gerado na LPT sera fornecido ao LPC. Cada qual com seu proprio eixo

Fico imensamente agradecido aos dois pelo apoio! Sou uma negacao em programacao kkk

Os parâmetros a serem utilizados, podem ser encontrados nas tabelas do arquivo “TCC Victor Barcellos” 
onde utilizarei os dados a nível do mar (se for possível ir alem, podemos fazer uma variação, mas focarei inicialmente a nível do mar).
