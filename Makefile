
# Variables to control Makefile operation

CC = g++
CFLAGS = -Wall -g

sorted-squared-array: sorted-squared-array.o
	$(CC) $(CFLAGS) -o sorted-squared-array sorted-squared-array.o

sorted-squared-array.o: sorted-squared-array.cpp
	$(CC) $(CFLAGS) -c sorted-squared-array.cpp

clean:
	rm -rf sorted-squared-array sorted-squared-array.o
