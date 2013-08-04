cat taxonomy_HEP.txt | sed 's/--- [A-Z] ---//g' > taxonomy_HEP.txt.step1
cat taxonomy_HEP.txt.step1 | sed 's/-.*//g' > taxonomy_HEP.txt.step2
cat taxonomy_HEP.txt.step2 | sed 's/\s*\[.*//g' > taxonomy_HEP.txt.step3
cat taxonomy_HEP.txt.step3 | sed 's/*\(.*\)/\1/g' > taxonomy_HEP.txt.step4
cat taxonomy_HEP.txt.step4 | sed 's/\s\(.*\)/\1/g' > taxonomy_HEP.txt.step5
cat taxonomy_HEP.txt.step5  | sed '/^$/d' > taxonomy_HEP.txt.step6
cat taxonomy_HEP.txt.step6 | uniq > taxonomy_HEP.txt.step7
cat taxonomy_HEP.txt.step7 | sed '/^\s*$/d' > taxonomy_HEP.txt.step8
cat taxonomy_HEP.txt.step8 | grep "(" -v > taxonomy_HEP.txt.step9
