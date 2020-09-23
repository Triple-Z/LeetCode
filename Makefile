# Thanks to https://github.com/kubernetes/ingress-nginx/blob/master/Makefile .

.DEFAULT_GOAL:=help

# set default shell
SHELL=/bin/bash -o pipefail -o errexit

.PHONY: help
help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z0-9_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

.PHONY: update-generate update-change
update-generate: ## Generate the new README file
	@python3 utils/update_readme.py -o README-generated.md
update-change: ## Replace the README file with newly generated one
	@mv README-generated.md README.md
	@echo "Changed README file successfully!"

.PHONY: update
update:  update-generate update-change ## Update the README file

.PHONY: new-doc ## Create a new doc from template
new-doc: # TODO
	@echo "TODO"