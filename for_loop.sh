#!/bin/bash

for value in {0..499}
do
	echo Handling output$value.sql
	mysql -u europeia_forum --password=ThreeONE3 europeia_forum < output$value.sql
done

echo All Done
