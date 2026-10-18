# C3 Fried Chicken — Django Website

A responsive Django website for C3 Fried Chicken with:
- Hero banner and C3 bucket branding (bucket has text/logo only, no chicken photo printed on it)
- Exactly 36 products transcribed from the supplied C3 menu: Broasted, Momos & Snacks, Burgers, Tea & Hot Drinks, Juices & Drinks, Extras
- Menu items editable through Django Admin
- Category filter, search, item detail pages
- WhatsApp ordering and tap-to-call buttons (no booking/reservation feature)
- Responsive mobile layout

## Requirements
- Python 3.10+
- 36 separate local product-image files cropped from the supplied C3 menu-board artwork. These are not verified camera photographs.

## Run locally (Windows)
1. Install Python from https://www.python.org/downloads/
2. Extract this ZIP.
3. Open Command Prompt in the extracted `c3_fried_chicken_django` folder.
4. Run:
   ```bat
   py -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   py manage.py makemigrations menu
py manage.py migrate
   py manage.py seed_menu
   py manage.py createsuperuser
   py manage.py runserver
   ```
5. Open http://127.0.0.1:8000/
6. Admin: http://127.0.0.1:8000/admin/ (use the superuser you created)

## Run locally (macOS/Linux)
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations menu
python manage.py migrate
python manage.py seed_menu
python manage.py createsuperuser
python manage.py runserver
```

## Customization
- Contact number is configured in `c3site/settings.py` as `CAFE_PHONE`; WhatsApp number is configured as `WHATSAPP_NUMBER` (country code included, digits only).
- Edit food items, prices, descriptions, category and photos from `/admin/`.
- Add your own images through Admin. For production, configure `MEDIA_ROOT`/`MEDIA_URL` and serve media using your hosting provider.
- Replace demo remote image URLs with your own licensed photographs if desired.

## Publish online with GitHub + Render

**Important:** GitHub stores your project files, but GitHub Pages cannot run Django/Python. To get a live website link, push this project to GitHub and deploy it on Render. The included `render.yaml` configures a Django web service and PostgreSQL database.

### A. Upload the project to GitHub
1. Sign in at https://github.com and create a new repository, e.g. `c3-fried-chicken-menu`.
2. Keep it private if you do not want the source code public (the website can still be public on Render).
3. Extract this ZIP on your computer.
4. In the extracted project folder, open Terminal / Command Prompt and run:
   ```bash
   git init
   git add .
   git commit -m "Prepare C3 menu website for hosting"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/c3-fried-chicken-menu.git
   git push -u origin main
   ```
   Replace `YOUR-USERNAME` with your GitHub username. Git must be installed and you must sign in when prompted.

### B. Create the live website
1. Open https://render.com and sign in using GitHub.
2. Choose **New + → Blueprint** (sometimes shown as “New Blueprint Instance”).
3. Select the `c3-fried-chicken-menu` GitHub repository.
4. Render reads `render.yaml`. Review the web service and PostgreSQL database, then create/deploy them.
5. Wait for the first deployment to finish. Render will provide a URL like `https://c3-fried-chicken-menu.onrender.com`.
6. Open that URL on phone, laptop, tablet and desktop to test the responsive menu. Use the URL for your QR code.

### C. Notes
- The build command installs dependencies, collects static files, runs migrations and seeds the 36 menu products.
- Do not upload `.venv/`, secret keys, or local `.env` files to GitHub.
- Free hosting/database availability and sleep/limits depend on Render's current plan. If the service sleeps, the first visit may take a little time to wake up.
- This project does not require GitHub Pages. Do not enable GitHub Pages for this Django app.
- Before launch, verify the shop's WhatsApp number and menu prices in `c3site/settings.py` and the menu data.
- Admin access is available at `/admin/` only after creating an admin account. For hosted admin access, create a superuser from the Render Shell with `python manage.py createsuperuser`.

## Menu accuracy update
The catalogue and bundled SQLite database contain exactly 36 menu products. French Fries is one product with Small ₹69 / Large ₹89 options; burger cheese prices are shown in each burger's description rather than being duplicated as separate products. Loaded Fries is listed at ₹169, retaining the printed PRC-179 note in its description. Each product has a separate local image file under `static/product-images/`.

## Deploy configuration
`render.yaml` is a Render Blueprint for deploying this Django project from GitHub. `requirements.txt` includes Gunicorn, WhiteNoise, PostgreSQL driver, and database URL configuration for production.
