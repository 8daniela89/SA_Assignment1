from document_editor import DocumentFactory

class CarManagementSystem:
    """Combines the two exercises."""
    
    def generate_order_document(self, car_builder, doc_format):
        # 1. Build car
        car = car_builder.build()
        
        # 2. Format details for the document
        details = f"ORDER DETAILS: Engine={car.engine}, Trans={car.transmission}"
        
        # 3. Create Document using factory
        doc = DocumentFactory.create_document(doc_format)
        
        # 4. Save and return result
        return doc.save(details)