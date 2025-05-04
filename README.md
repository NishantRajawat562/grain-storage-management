Here's a complete and polished README.md file for your Grain Storage Management System project:


---

# Grain Storage Management System

## Project by:
- **Nishant** – Backend & Database Developer
- **Sakshi** – Frontend Designer & UI Developer

___

# Project Video Google drive link

Here is a Google Drive link of Video Explanation Project

https://drive.google.com/file/d/1nsRwa2BlbF64PGyU19ITodDqeSVP6UA3/view?usp=sharing

___

# Project Report link

https://github.com/NishantRajawat562/grain-storage-management/blob/main/PROJECT%20REPORT.pdf


---

# Project link

https://github.com/NishantRajawat562/grain-storage-management/tree/main/Grain%20Market%20Storage%20System%20Project

___

## Project Overview

The **Grain Storage Management System** is a web-based application built using Python and Flask that streamlines the process of booking and managing grain storage. It is designed to bridge the gap between farmers and warehouse owners by providing a digital platform to handle storage booking and inventory management efficiently.

---

## Problem Statement

Farmers often face difficulties in finding and booking grain storage due to lack of digitization and real-time availability updates. Manual booking leads to overbooking or under-utilization of resources, affecting both farmers and warehouse owners.

---

## Proposed Solution

This project aims to:
- Digitally connect farmers and warehouse owners.
- Allow farmers to view and book available storage (in quintals).
- Let warehouse owners add, update, or delete storage entries.
- Automatically manage storage availability based on bookings.
- Provide farmer booking details to warehouse owners and allow booking cancellations.

---

## Features

### 1. Home Page
- View list of all storage availability (in quintals).

### 2. Warehouse Section
- Add, update, and delete storage.
- View farmer bookings with option to delete bookings and auto-update available storage.

### 3. Farmer Section
- Book storage by providing quantity, contact, address, and submission date.
- Booking allowed only one day before or on the date of submission.

---

## Technology Stack

| Layer        | Tools & Technologies                     |
|--------------|------------------------------------------|
| Frontend     | HTML, CSS, Bootstrap                     |
| Backend      | Python 3.13, Flask                       |
| Database     | SQLite (via `sqlite3`)                   |
| UI Design    | Bootstrap for responsive and clean UI    |

---

## Folder Structure

grain-storage-system/ ├── presentation.pptx ├── project_video.mp4 └── /src/ ├── app.py ├── static/ │   └── style.css ├── templates/ │   ├── base.html │   ├── home.html │   ├── warehouse.html │   └── farmer.html └── grain_storage.db

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/grain-storage-system

2. Navigate to the source folder:

cd grain-storage-system/src


3. Install Flask (if not already installed):

pip install flask


4. Run the app:

python app.py


5. Open the browser and go to:

http://127.0.0.1:5000


---

Conclusion

This project enhanced our understanding of web development, database integration, and project collaboration. It solves a real-world problem and can be extended in the future with login features, SMS notifications, and regional language support.



