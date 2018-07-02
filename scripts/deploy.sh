#!/bin/sh
export a=$(date +%d/%m/%Y)
cp --backup=numbered index.html backup/
cat index.html | sed -e "s;<p>Dernière mise à jour : .*<\/p>;<p>Dernière mise à jour : "$(date +%d/%m/%Y)"<\/p>;g" > temp.html
mv temp.html index.html
cp -Lr fichiers_liens/* fichiers/
cp -Lr info_liens/* info/
#netlify deploy
git commit -a
git push
