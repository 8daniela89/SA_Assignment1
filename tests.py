import unittest
import os
from car_configurator import CarBuilder
from document_editor import DocumentFactory, PdfDocument, HtmlDocument
from car_management import CarManagementSystem

class TestAssignment(unittest.TestCase):

    # --- Tests for builder (Car) ---
    def test_car_builder_success(self):
        builder = CarBuilder()
        car = (builder
               .set_engine("V8")
               .set_transmission("Automatic")
               .add_interior_feature("Leather Seats")
               .add_safety_feature("ABS")
               .build())
        
        self.assertEqual(car.engine, "V8")
        self.assertIn("Leather Seats", car.interior)

    def test_car_builder_validation(self):
        builder = CarBuilder()
        with self.assertRaises(ValueError):
            builder.build()

    # --- Tests for factory (Document) ---
    def test_factory_pdf(self):
        doc = DocumentFactory.create_document("pdf")
        self.assertIsInstance(doc, PdfDocument)
        # Check if the output string confirms file creation
        output = doc.save("Test Content")
        self.assertIn("created on disk", output)

    def test_factory_html(self):
        doc = DocumentFactory.create_document("html")
        output = doc.save("Test Content")
        self.assertIn("created on disk", output)

    def test_factory_invalid(self):
        with self.assertRaises(ValueError):
            DocumentFactory.create_document("unknown_format")

    # --- Tests for integration ---
    def test_integration(self):
        cms = CarManagementSystem()
        builder = CarBuilder().set_engine("V6").set_transmission("Manual")
        output = cms.generate_order_document(builder, "pdf")
        
        # check if the integration returns the success message
        self.assertIn("created on disk", output)

    # Cleanup-remove files created during testing
    def tearDown(self):
        files_to_remove = ["document.pdf.txt", "document.docx.txt", "index.html"]
        for f in files_to_remove:
            if os.path.exists(f):
                os.remove(f)

if __name__ == "__main__":
    unittest.main()