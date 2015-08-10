all: main.o functions.o
		gcc main.o functions.o -o bin/converter -lm
 
main.o: main.c functions.h
		gcc -c main.c -o main.o
 
functions.o: functions.c
		gcc -c functions.c -o functions.o
 
clean:
		rm -rf *.o
 
mrproper: clean
		rm -rf converter
