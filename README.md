# Robô de teste — Pop-up (RPA Brasil)

Robô de exemplo para testar a instalação de automações **direto de um
repositório Git** na Control Room do
[Template Python RPA Brasil](https://github.com/arthurfs11/Template_Python_RPA_Brasil).

## O que ele faz

Abre um **pop-up nativo** na tela da máquina onde o agente roda (no macOS usa
`osascript`/`display dialog`). Serve para confirmar visualmente que um job da
Control Room chegou até a máquina e foi executado.

O pop-up fecha sozinho após 30 segundos (ou ao clicar em OK).

## Como usar na Control Room

1. Abra a Control Room → aba **Automações**
2. Em **Instalar do Git**, informe a URL deste repositório:

   ```
   https://github.com/arthurfs11/robo-teste-popup.git
   ```

   (branch/tag é opcional — deixe vazio para usar o padrão)
3. Clique em **Instalar do Git**. O robô aparece na lista (tag **git**)
4. Dispare o processo **teste_popup** para uma máquina e veja o pop-up

Depois de instalado, o botão **Atualizar** clona o repositório de novo e
substitui a versão em uso com um clique.

## Estrutura

```
rpa.json   → manifesto do robô (nome, entrada, função, etc.)
main.py    → função `rodar()` que o agente executa
```

## Fora da Control Room

```bash
python -m core.control_room.pacote instalar-git https://github.com/arthurfs11/robo-teste-popup.git
```
