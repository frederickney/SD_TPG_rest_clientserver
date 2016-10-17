HEADERS := $(wildcard *.py)

doc: doc_python/index.html

doc_python/index.html: Doxyfile_python $(HEADERS) $(SOURCES)
	@echo "generating doc with doxygen..."
	@doxygen Doxyfile_python

clean_doc:
	@echo "cleaning doc..."
	@rm -rf doc_python