.PHONY: install fetch help test build summarize run

UV = $(HOME)/.local/bin/uv

help:
	@echo "Usage:"
	@echo "  make install                                        Install dependencies and Playwright browser"
	@echo "  make fetch                                          Fetch transcripts from start of current month"
	@echo "  make fetch SINCE=YYYY-MM-DD                         Fetch transcripts from a specific date through today"
	@echo "  make fetch BETWEEN=YYYY-MM-DD/YYYY-MM-DD            Fetch transcripts within a date range"
	@echo "  make fetch SIG=<slug>                               Fetch transcripts for a specific SIG only"
	@echo "  make fetch SINCE=YYYY-MM-DD SIG=<slug>              Combine date and SIG filters"
	@echo "  make test                                           Run tests"
	@echo "  make build                                          Build docs/ site from transcripts"
	@echo "  make summarize                                      Generate AI summaries (requires OPENAI_API_KEY)"
	@echo "  make run                                            Serve docs/ site locally on http://localhost:8000"

install:
	$(UV) sync
	$(UV) run playwright install chromium

fetch:
ifdef BETWEEN
	$(UV) run python main.py --between $(word 1,$(subst /, ,$(BETWEEN))) $(word 2,$(subst /, ,$(BETWEEN))) $(if $(SIG),--sig $(SIG),)
else
	$(UV) run python main.py $(if $(SINCE),--since $(SINCE),) $(if $(SIG),--sig $(SIG),)
endif

test:
	$(UV) run --group dev pytest tests/ -v

build:
	$(UV) run python build_site.py

summarize:
	$(UV) run --group summarize python generate_summaries.py
	$(UV) run python build_site.py

run:
	python3 -m http.server 8000 --directory docs
