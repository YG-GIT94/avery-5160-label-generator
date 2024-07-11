User Story: Generate SKU Labels from PDF Barcode Files
Title
As a user, I want to generate Avery 5160 labels from PDF barcode files, so that I can easily print and use them.

Description
The SKU Labels Generator application allows users to select one or more PDF files containing barcode images and generate Avery 5160 labels from those images. The output will include a header with the original filename and the labels will be saved in a user-specified directory.

Acceptance Criteria
File Selection:

Given the application is running,
When I open the file selection dialog,
Then I can select one or more PDF files containing barcode images.
Output Directory Selection:

Given the application is running,
When I open the directory selection dialog,
Then I can specify an output directory where the generated label PDF files will be saved.
Label Generation:

Given I have selected PDF files and an output directory,
When I start the label generation process,
Then the application extracts barcode images from each PDF file,
And generates a new PDF file formatted as Avery 5160 labels for each input file,
And includes a header with the original filename (without the extension) at the top of each generated PDF.
Completion Notification:

Given the label generation process is complete,
When the application finishes processing,
Then I receive a notification that the process is complete,
And I can see the location of the saved files.
Tasks
Implement the file selection dialog using tkinter.
Implement the output directory selection dialog using tkinter.
Extract barcode images from the selected PDF files using PyMuPDF.
Generate Avery 5160 labels using ReportLab and include a header with the filename.
Implement user notifications for process completion.
Definition of Done
The application allows users to select PDF files and an output directory.
Barcode images are correctly extracted from the selected PDF files.
Avery 5160 labels are generated with a header containing the original filename.
The generated PDF files are saved in the specified output directory.
Users are notified upon completion of the label generation process.
