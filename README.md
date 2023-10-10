🚀 Astrid's G-Maps Scan 🚀
Olá, exploradores de APIs! 🕵️‍♂️ Bem-vindo ao Astrid's G-Maps Scan, a sua nova ferramenta favorita para verificar a vulnerabilidade das suas chaves API do Google Maps de uma maneira rápida, visual e super amigável!

🎯 Objetivo
Este script Python foi desenvolvido com o objetivo de fornecer um feedback visual rápido e eficiente sobre a vulnerabilidade das suas chaves API do Google Maps em várias APIs. Ele é modular e escalável, permitindo que você adicione mais URLs para verificar conforme necessário. E o bônus: você pode exportar os resultados para um .txt como POC e evidência!

🛠️ Como Funciona
O script verifica a vulnerabilidade das chaves API em várias APIs do Google Maps, apresentando os resultados de forma clara e colorida no console. Ele verifica uma lista de URLs (que você pode expandir!) e retorna se a chave API é vulnerável ou não, juntamente com algumas informações adicionais, como custo por solicitação.

🚗 Começando
Instalação de Dependências

Antes de começar, certifique-se de que tem todas as bibliotecas necessárias instaladas. Se não, apenas corra o seguinte comando no seu terminal:

bash
Copy code
pip install requests colorama
Chave API

Você vai precisar de uma chave API do Google Maps para testar. Se você não tem uma ainda, pode obter uma aqui.

Execução

Execute o script Python no seu terminal com:

bash
Copy code
python nome_do_script.py
E siga as instruções na tela para inserir a sua chave API e começar a verificação!

📋 Exportando Resultados
No final da execução, o script irá perguntar se você deseja exportar os resultados para um arquivo .txt. Isso pode ser útil para manter um registro das APIs vulneráveis e usar como prova de conceito ou evidência.

🔄 Extensibilidade
Sinta-se à vontade para adicionar mais URLs para verificar! Basta adicionar uma nova tupla na lista urls_to_check com o formato:

python
Copy code
("URL", "MÉTODO", "DESCRIÇÃO", "CUSTO", DADOS_POST)
🤝 Contribuindo
Adoraríamos ver as suas contribuições! Sinta-se à vontade para adicionar novas funcionalidades, corrigir bugs ou melhorar a documentação. Basta fazer um fork e enviar um Pull Request!

📜 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE.md para mais detalhes.

🎉 Agradecimentos
Um grande obrigado a todos que contribuíram e que vão contribuir no futuro!

🚀 Vamos explorar o universo das APIs juntos! 🚀
