DESTDIR = bin
SRCDIR = src
INCDIR = include
OBJDIR = $(DESTDIR)/obj
DIRS = $(BINDIR) $(OBJDIR)
installdir = mkdir

CC = gcc
CFLAGS = -I $(INCDIR) -c

LINKER = LD
LDFLAGS = 

CFILES = $(wildcard $(SRCDIR)/*.c)
OBJFILES = $(foreach obj,$(CFILES),$(obj:$(SRCDIR)/%.c=$(OBJDIR)/%.o))
EXEFILES = $(foreach obj,$(CFILES),$(obj:$(SRCDIR)/%.c=$(DESTDIR)/%))

all: $(DIRS) $(OBJFILES)
$(DIRS):$(SRCDIR)
	$(installdir) -p $(DIRS)

$(OBJDIR)/%.o:$(SRCDIR)/%.c
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm $(DESTDIR) -rf
.PHONY: all
