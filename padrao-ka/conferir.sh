#!/bin/bash
# Confere se algum texto vazou do painel (o fundo do painel esta em 9,60").
#
#   padrao-ka/conferir.sh <arquivo.pptx>
#
# Converte com o LibreOffice e mede a caixa real de cada palavra com
# pdftotext -bbox — as alturas declaradas no python-pptx sao so um chute, o
# texto quebra em mais linhas do que se espera.
#
# A previa so diz a verdade com as 12 fontes de padrao-ka/fontes/ instaladas
# (padrao-ka/instalar-fontes.sh). Sem elas o LibreOffice cai na DejaVu Sans,
# que e mais larga, e a conferencia acusa vazamento onde nao ha.
set -e
SRC=$(readlink -f "${1:?uso: conferir.sh <arquivo.pptx>}")
AQUI=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d)
mkdir -p "$T/x" && cd "$T/x"
unzip -o -q "$SRC"
zip -q -r ../previa.pptx . && cd "$T"
# perfil proprio por execucao: duas conferencias ao mesmo tempo disputam o
# perfil padrao do LibreOffice e as duas travam sem dizer nada
timeout 500 soffice -env:UserInstallation="file://$T/lo" \
  --headless --norestore --convert-to pdf --outdir . previa.pptx >/dev/null 2>&1
pdftoppm -png -r 62 previa.pdf s
pdftotext -bbox previa.pdf bb.html 2>/dev/null
python3 "$AQUI/conferir.py" "$T/bb.html"
echo "previa em PNG: $T/s-*.png"
