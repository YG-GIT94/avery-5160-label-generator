# User Stories

## User Story 1: Extract Invoice Data

**Title:** Extract Invoice Data from QuickBooks PDFs  
**As a** user  
**I want to** extract invoice data from multiple QuickBooks PDF invoices  
**So that** I can process and analyze the invoice information efficiently  

### Tasks
- Implement a function to open and read multiple PDF files.
- Use regex to extract the invoice number, bill-to information, and invoice table data.
- Add filtering conditions for the data.

### Acceptance Criteria
- **Given** I have multiple QuickBooks PDF invoices  
  **When** I run the script  
  **Then** I should be able to select multiple PDF files  
  **And** the script should extract the invoice number, bill-to information, and invoice table data  
  **And** the data should be filtered based on specified conditions which can be modified as needed  

### Definition of Done
- Code is written and reviewed.
- Unit tests are created and pass.
- Documentation is updated with usage instructions.
- The script successfully extracts data from sample PDFs.

---

## User Story 2: Create Excel Template

**Title:** Create an Excel Template for Import  
**As a** user  
**I want to** create an Excel template based on the current system import mapping  
**So that** I can ensure the extracted data is mapped correctly  

### Tasks
- Define the structure of the Excel template.
- Implement a function to create the Excel template with the specified structure.
- Ensure column headers and formatting are correctly applied.

### Acceptance Criteria
- **Given** I have run the script  
  **When** the script generates an Excel template  
  **Then** the template should have predefined column headers and formatting  
  **And** it should include all necessary columns for order information and product details  

### Definition of Done
- Code is written and reviewed.
- Unit tests are created and pass.
- Documentation is updated with template structure details.
- The script successfully creates the template with correct formatting.

---

## User Story 3: Map Data to Excel Template

**Title:** Map Extracted Data to Excel Template  
**As a** user  
**I want to** map the extracted invoice data to the generated Excel template  
**So that** I can have a structured and organized representation of the invoice data  

### Tasks
- Implement a function to map the extracted data to the corresponding columns in the template.
- Ensure data alignment and handle any formatting issues.
- Auto-fit column widths based on content.

### Acceptance Criteria
- **Given** I have extracted invoice data and generated an Excel template  
  **When** the script maps the data to the template  
  **Then** the data should be correctly aligned with the corresponding columns  
  **And** there should be no empty rows between mapped data  
  **And** the column widths should auto-fit the content  

### Definition of Done
- Code is written and reviewed.
- Unit tests are created and pass.
- Documentation is updated with mapping details.
- The script successfully maps data to the template without errors.

---

## User Story 4: Provide Feedback on Completion

**Title:** Notify User Upon Successful Template Creation  
**As a** user  
**I want to** receive a notification upon the successful creation and saving of the Excel template  
**So that** I know the process has been completed  

### Tasks
- Implement a notification function to display a message box upon completion.
- Ensure the message box displays the correct information about the saved template.

### Acceptance Criteria
- **Given** the script has finished processing the PDF invoices and saved the Excel template  
  **When** the process is complete  
  **Then** a message box should display confirming the successful creation and saving of the template  

### Definition of Done
- Code is written and reviewed.
- Unit tests are created and pass.
- Documentation is updated with completion notification details.
- The script successfully displays the message box upon completion.
