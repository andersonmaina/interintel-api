# InterIntel Bulk Notification API — Option A


## Setup(primarily windows)

```bash
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate
```

```bash
# On Linux or Mac(use python3 onwards instead of py or python)
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python3 manage.py migrate
```

## Run

```bash
python manage.py runserver
```

Server runs at `http://127.0.0.1:8000/`.

## Endpoint

```
POST /api/notifications/bulk/
```



## Test with cURL

```bash
# Windows (cmd):
curl -X POST http://127.0.0.1:8000/api/notifications/bulk/ -H "Content-Type: application/json" -d "{\"name\": \"Alice Kamau\", \"email\": \"njoro@example.com\", \"notifications\": [{\"title\": \"Welcome\", \"channel\": \"email\", \"message\": \"Thank you for joining us.\"}, {\"title\": \"Reminder\", \"channel\": \"sms\", \"message\": \"Your subscription renews tomorrow.\"}]}"
```

```bash
# Linux/Mac:
curl -X POST http://127.0.0.1:8000/api/notifications/bulk/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Njoro Maina",
    "email": "njoro@example.com",
    "notifications": [
      {"title": "Welcome", "channel": "email", "message": "Thank you for joining us."},
      {"title": "Reminder", "channel": "sms", "message": "Your subscription renews tomorrow."}
    ]
  }'
```

## Tests

```bash
python manage.py test notifications
```

Run individually:

```bash
python manage.py test notifications.tests.test_serializers #for testing serializers validation logic
python manage.py test notifications.tests.test_services #for testing service logic
```


## Test with Postman

1.Open Postman and create a new request.
2.Set the method to **POST**.
3.Set the URL to:
   ```
   http://127.0.0.1:8000/api/notifications/bulk/
   ```
4.Go to the **Headers** tab and add:
   ```
   Key: Content-Type
   Value: application/json
   ```
5.Go to the **Body** tab, select **raw**, and choose **JSON** from the dropdown on the right.

6.Paste the sample request:
   ```json
   {
     "name": "Njoro Maina",
     "email": "njoro@example.com",
     "notifications": [
       {
         "title": "Welcome",
         "message": "Thank you for joining us.",
         "channel": "email"
       },
       {
         "title": "Reminder",
         "message": "Your subscription renews tomorrow.",
         "channel": "sms"
       }
     ]
   }
   ```
7.Click **Send**. You should get a `201 Created` response with `"success": true` and the created notifications.

## Confirm data presence in admin
 
1.Create a superuser if you haven't already:
```bash
   python manage.py createsuperuser
```
```bash
   # On Linux or Mac:
   python3 manage.py createsuperuser
```
2.Start the server if it isn't running:
```bash
   python manage.py runserver
```
3.Open your browser and go to:
```
   http://127.0.0.1:8000/admin/
```
4.Log in with your superuser credentials.

5.Click **Senders** to confirm the sender was created.

6.Click **Notifications** to confirm all notifications were created.
