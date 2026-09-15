#!/bin/bash
# Confere se algum texto vazou do painel (o fundo do painel esta em 9,60").
#
#   padrao-ka/conferir.sh <arquivo.pptx>
#
# Converte com o LibreOffice e mede a caixa real de cada palavra com
# pdftotext -bbox — as alturas declaradas no python-pptx sao so um chute, o
# texto quebra em mais linhas do que se espera.
#
# A copia usada na conferencia troca "Outfit 2 Semi-Bold" por
# "Outfit 2 SemiBold" porque o fontconfig local nao casa o nome com hifen e
# substitui por DejaVu Sans, fazendo a previa mentir sobre o peso. O arquivo
# ENTREGUE nunca e alterado.
set -e
SRC=$(readlink -f "${1:?uso: conferir.sh <arquivo.pptx>}")
AQUI=$(cd "$(dirname "$0")" && pwd)
T=$(mktemp -d)
mkdir -p "$T/x" && cd "$T/x"
unzip -o -q "$SRC"
sed -i 's/Outfit 2 Semi-Bold/Outfit 2 SemiBold/g' ppt/slides/slide*.xml
zip -q -r ../previa.pptx . && cd "$T"
timeout 500 soffice --headless --norestore --convert-to pdf \
  --outdir . previa.pptx >/dev/null 2>&1
pdftoppm -png -r 62 previa.pdf s
pdftotext -bbox previa.pdf bb.html 2>/dev/null
python3 "$AQUI/conferir.py" "$T/bb.html"
echo "previa em PNG: $T/s-*.png"
