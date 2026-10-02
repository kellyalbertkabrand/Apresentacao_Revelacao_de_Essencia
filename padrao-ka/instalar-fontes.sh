#!/bin/bash
# Instala as fontes do padrao KA para o usuario e refaz o cache.
#
#   padrao-ka/instalar-fontes.sh
#
# Sem isso o LibreOffice nao acha a Outfit e substitui por DejaVu Sans, que e
# mais larga: a previa fica feia e a conferencia de vazamento acusa erro onde
# nao ha. As fontes sao as mesmas que vem embarcadas no arquivo da Kelly.
set -e
AQUI=$(cd "$(dirname "$0")" && pwd)
mkdir -p "$HOME/.fonts"
cp "$AQUI"/fontes/*.ttf "$HOME/.fonts/"
fc-cache -f >/dev/null
echo "fontes instaladas:"
fc-list | grep -iE "outfit|playfair|plex" | sed 's/.*: //' | sort -u
