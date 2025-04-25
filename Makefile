install:
	uv sync

build:
	uv build

package-install:
	uv tool install dist/*.whl

reinstall-package:
	uv tool install --force dist/*.whl

gendiff:
	uv run gendiff