# ETL de Dados com Dataset do Netflix

## Contexturalização

Suponhamos que trabalhamos para a Netflix e temos arquivos de dados em formato .xlxs com dados de novos assinantes, que chegam diariamente. Por dia chegam em média de 20 a 30 arquivos.

Com base nesses aruqivos seu chefe lhe diz que precisa de um Dashboard com os dados dos novos assinantes e de quais campanhas de marketing eles vieram.

### Desafio

Esses arquivos não estão padronizados e eles vem de diversos países.

Para o Dashboard precisamos que esses arquivos estejam juntos em um único arquivo .csv e ainda as informações dos arquivos não estão da forma que são necessárias para exibir no Dashboard.

Precisamos tratar os dados, consolidá-los e deixá-los prontos para consumo do Dashboard. Por exemplo, para exibição no Dashboard vamos precisar de trazer apenas a campanha que está no link da UTM e não o link completo.

Além disso é necessário manter a rastreabilidade dos dados, pois o país de origem dos dados está específicado somente no nome do arquivo e não nas informações presentes no arquivo.

##### Dataset com arquivos .xlxs disponível em https://github.com/digitalinnovationone/netflix-dataset.git

O arquivo possui a seguinte estrutura:

sale_date -> Data da assinatura

Customer -> Nome do cliente que fez a assinatura

Contracted Plan -> Plano contratado

Amount -> Valor da assinatura

utm_link -> Link personalizado com campanha utilizada para rastrear a origem da assinatura

Age -> Idade do assintante
