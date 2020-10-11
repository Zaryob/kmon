all:

install:
	mkdir -p $(DESTDIR)/usr/local/bin
	mkdir -p $(DESTDIR)/usr/local/share/man/man8
	cp kmon $(DESTDIR)/usr/local/bin
	cp kmon.8 $(DESTDIR)/usr/local/share/man/man8

uninstall:
	rm -f $(DESTDIR)/usr/local/bin/kmon
	rm -f $(DESTDIR)/usr/local/share/man/man8/kmon.8
