from abc import ABC,abstractmethod

class DocumentElement(ABC):
     
    @abstractmethod
    def RenderDocument(self):
        pass

class TextElement(DocumentElement):

    def __init__(self, text):
        self.text = text

    def RenderDocument(self):
        return self.text
    
class ImageElement(DocumentElement):

    def __init__(self, image_path):
        self.image_path = image_path
    
    def RenderDocument(self):
        return f"Image added at {self.image_path}"
    

class Document:
    def __init__(self):
        
        self.list_document_elements : list[DocumentElement] = []

    def add_element(self, element: DocumentElement):
        self.list_document_elements.append(element)

    def get_elements(self):
        return self.list_document_elements
    
    def render(self):
        return "\n".join(element.RenderDocument() for element in self.list_document_elements)
        
class Persistence(ABC):
    @abstractmethod
    def SaveDocument(self, data):
        pass

class SaveToFile(Persistence):
    def __init__(self, filename="Enter Filename to save data"):
        self.filename = filename+".txt"

    def SaveDocument(self, data):
        
        try:
            with open(self.filename, "w") as file:
                file.write(data)
            print("Document saved to document.txt")
        except IOError:
            print("Error: Unable to open file for writing.")
    
class SaveToDb(Persistence):

    def SaveDocument(self, data):
        raise NotImplementedError("Saving to database is not implemented yet.")
    
class DocumentEditor:

    def __init__(self, document: Document, storage: Persistence):
        self.document = document
        self.storage = storage
        self.rendered_document = None

    def add_text(self, text):
        self.document.add_element(TextElement(text))

    def add_image(self, image_path):
        self.document.add_element(ImageElement(image_path))

    def render_document(self):
        if not self.rendered_document:
            self.rendered_document = self.document.render()
        return self.rendered_document


    def save_document(self):
        self.storage.SaveDocument(self.render_document())




# Example usage
if __name__ == "__main__":
    document = Document()
    persistence = SaveToFile("Document1")
    editor = DocumentEditor(document, persistence)

    editor.add_text("Hello, world!")
   
    editor.add_text("This is a real-world document editor example.")
   
    
    editor.add_image("picture.jpg")

    print(editor.render_document())
    editor.save_document()


