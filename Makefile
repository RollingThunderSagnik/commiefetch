PREFIX?=/usr
BIN?=$(PREFIX)/bin

default:
	@printf "Usage:\n\tmake install\tinstall commiefetch\n\tmake uninstall\tuninstall commiefetch\n"
install:
	install -Dm755 commiefetch $(BIN)/commiefetch
	install -Dm755 commiefetchpy $(BIN)/commiefetchpy
uninstall:
	rm -f $(BIN)/commiefetch
	rm -f $(BIN)/commiefetchpy