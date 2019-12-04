resultado.png : datos.dat plot.py
	python plot.py

datos.dat : punto17.x
	./punto17.x

punto17.x : punto17.cpp punto15.py
	python punto15.py
	c++ punto17.cpp -o punto17.x
	
clean : 
	rm sigma.png datos.dat punto17.x resultado.png