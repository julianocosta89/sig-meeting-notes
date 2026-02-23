.PHONY: install fetch help

UV = $(HOME)/.local/bin/uv

help:
	@echo "Usage:"
	@echo "  make install                           Install dependencies and Playwright browser"
	@echo "  make fetch                             Fetch transcripts from start of current month"
	@echo "  make fetch SINCE=YYYY-MM-DD            Fetch transcripts from a specific date through today"
	@echo "  make fetch BETWEEN=YYYY-MM-DD/YYYY-MM-DD   Fetch transcripts within a date range"

install:
	$(UV) sync
	$(UV) run playwright install chromium

fetch:
ifdef BETWEEN
	$(UV) run python main.py --between $(word 1,$(subst /, ,$(BETWEEN))) $(word 2,$(subst /, ,$(BETWEEN)))
else
	$(UV) run python main.py $(if $(SINCE),--since $(SINCE),)
endif
