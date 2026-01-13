from abc import ABC, abstractmethod

class Document(ABC):
    @abstractmethod
    def save(self, content):
        pass
    @abstractmethod
    def display(self):
        pass

class PdfDocument(Document):
    def save(self, content):
        # simulate creating a file by writing a .txt file named .pdf
        filename = "document.pdf.txt"
        with open(filename, "w") as f:
            f.write(f"[PDF HEADER] \n{content}")
        return f"File '{filename}' created on disk."

    def display(self):
        return "Opening Adobe Acrobat Reader..."

class WordDocument(Document):
    def save(self, content):
        filename = "document.docx.txt"
        with open(filename, "w") as f:
            f.write(f"[WORD HEADER] \n{content}")
        return f"File '{filename}' created on disk."

    def display(self):
        return "Opening Microsoft Word..."

class HtmlDocument(Document):
    def save(self, content):
        filename = "index.html"
        with open(filename, "w") as f:
            f.write(f"<html><body>{content}</body></html>")
        return f"File '{filename}' created on disk."

    def display(self):
        return "Opening Google Chrome..."

# ... (Keep the DocumentFactory class exactly as it was) ...
class DocumentFactory:
    @staticmethod
    def create_document(doc_type):
        doc_types = {
            "pdf": PdfDocument,
            "word": WordDocument,
            "html": HtmlDocument
        }
        doc_class = doc_types.get(doc_type.lower())
        if doc_class:
            return doc_class()
        raise ValueError(f"Unknown document type: {doc_type}")