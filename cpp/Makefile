CC = gcc
CFLAGS = -I$(INCDIR)

INCDIR = include
BINDIR = bin
OBJDIR = obj

ALL = 

$(OBJDIR)/%.o: %.c
	@[ -d $(OBJDIR) ] || mkdir $(OBJDIR)
	$(CC) -c -o $@ $< $(CFLAGS)

all: $(ALL)

add: $(patsubst %, $(OBJDIR)/%, add.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -o $(BINDIR)/$@ $^ $(CFLAGS)

run-%: $(BINDIR)/%
	$^

runall: all
	@echo -e
	@for exe in $(ALL); do \
		echo "$(BINDIR)/$$exe"; \
		$(BINDIR)/$$exe; \
		echo -e; \
	done


.PHONY: clean
clean:
	rm -rf $(BINDIR) $(OBJDIR)
