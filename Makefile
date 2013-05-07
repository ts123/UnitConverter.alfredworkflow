TARGET=UnitConverter.alfredworkflow
SOURCES=$(shell /bin/ls -1 info.plist *.py *.png img/*.png Makefile README.md)

.PHONY: all clean install list

all: $(TARGET)

$(TARGET): $(SOURCES)
	zip $(TARGET) $(SOURCES)

clean:
	rm -rf $(TARGET)

install:
	open $(TARGET)

list:
	unzip -l $(TARGET)

