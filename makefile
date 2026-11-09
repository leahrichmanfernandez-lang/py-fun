.PHONY: build install run tests package clean

build: clean install tests package

install:
	pip install -r requirements.txt

run:
	python3 -c "import src.main as m; m.main()"

tests:
	pytest

package:
	mkdir -p build/lib
	cp -r src build/lib/
	cp -r tests build/lib/
	tar -czf py-fun-SNAPSHOT-0.1.0.tar -C build/lib .

clean:
	rm -rf build py-fun-SNAPSHOT-0.1.0.tar
	