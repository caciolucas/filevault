# FileVault

**FileVault** is a simple Django application designed to store and manage files for different clients. All actions—such as adding, editing, and deleting both clients and their files—are performed seamlessly within the Django Admin interface. The goal is to provide a straightforward file management solution with minimal complexity.

---

## Features

1. **Client Management**  
   - Add and edit client records through Django Admin.  
   - Store essential client information (e.g., name, contact, etc.).

2. **File Storage**  
   - Upload and associate files with each client.  
   - View and manage these files from the Django Admin (upload new, replace existing, or delete).

3. **Admin Interface**  
   - Leverages Django’s default admin site for easy CRUD operations.  
   - Secured by Django’s built-in authentication.

---

## Usage

1. **Add a Client**  
   - Go to **Clients** in Django Admin and click **Add**.  
   - Enter the client’s information and save.

2. **Upload Files**  
   - Go to **Files** in Django Admin and click **Add**.  
   - Select the relevant client and upload the file.

3. **Manage Files**  
   - Use the Django Admin to view, update, or delete existing files.
