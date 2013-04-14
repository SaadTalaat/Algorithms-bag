DESTDIR = bin
SRCDIR = src
INCDIR = include
OBJDIR = $(DESTDIR)/obj
TESTDIR = tests
TDIR = $(DESTDIR)/tests
DIRS = $(BINDIR) $(OBJDIR) $(TDIR)

installdir = mkdir

CC = gcc
CFLAGS = -I $(INCDIR) 

LINKER = LD
LDFLAGS = 

CFILES = $(wildcard $(SRCDIR)/*.c)
TFILES = $(wildcard $(TESTDIR)/*.c)
OBJFILES = $(foreach obj,$(CFILES),$(obj:$(SRCDIR)/%.c=$(OBJDIR)/%.o))
TESTFILES = $(foreach obj,$(TFILES),$(obj:$(TESTDIR)/%.c=$(TDIR)/%))
EXEFILES = $(foreach obj,$(CFILES),$(obj:$(SRCDIR)/%.c=$(DESTDIR)/%))

all: $(DIRS) $(OBJFILES)
$(DIRS):$(SRCDIR)
	$(installdir) -p $(DIRS)

$(OBJDIR)/%.o:$(SRCDIR)/%.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm $(DESTDIR) -rf
tests:$(TESTFILES)
	$(foreach test,$(TESTFILES),$(test))
$(TDIR)/%: $(TESTDIR)/%.c
	$(CC) $(CFLAGS)  $< $(OBJFILES) -o $@ -lcheck_pic
.PHONY: all
