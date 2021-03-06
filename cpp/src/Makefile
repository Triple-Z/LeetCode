CC = g++
CFLAGS = -I$(INCDIR) -std=c++11 -Wall -Wextra

INCDIR = ../include
BINDIR = ../bin
OBJDIR = ../obj

ALL = 905 832 1 15 16 18 26 27 80 11 35 53 121 122 123 66 697 88

$(OBJDIR)/%.o: %.cpp
	@[ -d $(OBJDIR) ] || mkdir $(OBJDIR)
	$(CC) -c -g -o $@ $< $(CFLAGS)

all: $(ALL)

88: $(patsubst %, $(OBJDIR)/%, 88.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

697: $(patsubst %, $(OBJDIR)/%, 697.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

66: $(patsubst %, $(OBJDIR)/%, 66.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

123: $(patsubst %, $(OBJDIR)/%, 123.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

122: $(patsubst %, $(OBJDIR)/%, 122.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

121: $(patsubst %, $(OBJDIR)/%, 121.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

53: $(patsubst %, $(OBJDIR)/%, 53.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

35: $(patsubst %, $(OBJDIR)/%, 35.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

11: $(patsubst %, $(OBJDIR)/%, 11.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

80: $(patsubst %, $(OBJDIR)/%, 80.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

27: $(patsubst %, $(OBJDIR)/%, 27.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

26: $(patsubst %, $(OBJDIR)/%, 26.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

18: $(patsubst %, $(OBJDIR)/%, 18.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

16: $(patsubst %, $(OBJDIR)/%, 16.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

15: $(patsubst %, $(OBJDIR)/%, 15.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

1: $(patsubst %, $(OBJDIR)/%, 1.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

832: $(patsubst %, $(OBJDIR)/%, 832.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

905: $(patsubst %, $(OBJDIR)/%, 905.o)
	@[ -d $(BINDIR) ] || mkdir $(BINDIR)
	$(CC) -g -o $(BINDIR)/$@.out $^ $(CFLAGS)

run-%: $(BINDIR)/%.out
	$^

debug-%: $(BINDIR)/%.out
	gdb $^

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
