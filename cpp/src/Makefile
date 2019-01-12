CC = g++
CFLAGS = -I$(INCDIR)

INCDIR = ../include
BINDIR = ../bin
OBJDIR = ../obj

ALL = 905

$(OBJDIR)/%.o: %.cpp
	@[ -d $(OBJDIR) ] || mkdir $(OBJDIR)
	$(CC) -c -g -o $@ $< $(CFLAGS)

all: $(ALL)

905: $(patsubst %, $(OBJDIR)/%, 905.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

run-%: $(BINDIR)/%.out
	$^

runall: all
	@echo -e
	@for exe in $(ALL); do \
		echo "$(BINDIR)/$$exe.out"; \
		$(BINDIR)/$$exe.out; \
		echo -e; \
	done


.PHONY: clean
clean:
	rm -rf $(BINDIR) $(OBJDIR)
