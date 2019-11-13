#!/bin/sh
export a=$(date +%d/%m/%Y)
cp --backup=numbered index.html backup/
cat index.html | sed -e "s;<p>Dernière mise à jour : .*<\/p>;<p>Dernière mise à jour : "$(date +%d/%m/%Y)"<\/p>;g" > temp.html
mv temp.html index.html
scripts/maj_liens.sh
#netlify deploy
git commit -a -m $(date +%d/%m/%Y)
git push
