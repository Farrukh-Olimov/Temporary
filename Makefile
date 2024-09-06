CPP :=g++
LDFLAGS :=
CPP_SOURCES :=$(shell find . -name "*.cpp")
CPP_EXECUTABLE :=$(CPP_SOURCES:.cpp=)

.PHONY: build-source
build-source:$(CPP_EXECUTABLE)

$(CPP_EXECUTABLE):$(CPP_SOURCES)
		$(CPP) $< $(LDFLAGS) $(CFLAGS) -o $@.o

.PHONY: clean-source
clean-source:
	find . -name "*.cpp" -type f -delete

.PHONE: clean-binary
clean-binary:
	find . -name "*.o" -type f -delete

