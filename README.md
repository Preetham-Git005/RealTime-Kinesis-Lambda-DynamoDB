# Real-Time Data Ingestion using AWS Kinesis, Lambda, and DynamoDB 🚀

This project demonstrates a real-time data ingestion pipeline using **AWS Kinesis**, **AWS Lambda**, and **Amazon DynamoDB**. It captures user activities and stores them in a DynamoDB table with near real-time processing.

---

## 🛠️ Tools & Services Used

- **AWS Kinesis Data Stream**
- **AWS Lambda**
- **Amazon DynamoDB**
- **AWS CLI**
- **Python (Boto3)**

---

## 📌 Architecture

1. A JSON record is encoded in Base64 and pushed into **Kinesis** via CLI.
2. **Lambda** is triggered as a **Kinesis consumer**.
3. Lambda decodes the event, extracts fields like `username`, `action`, and `timestamp`.
4. The extracted data is stored into the **DynamoDB** table `useractions`.

---

## ⚙️ Sample Kinesis CLI Command

Use this to push data into the Kinesis stream (Base64-encoded JSON):

```bash
aws kinesis put-record --stream-name data-stream-demo --partition-key "user1" \
--data "eyJ1c2VybmFtZSI6InNhaV9wcmVldGhhbSIsImFjdGlvbiI6ImxvZ2luIiwidGltZXN0YW1wIjoiMjAyNS0wNy0yNVQxNDowMDowMFoifQ==" \
--region ap-south-1
```

---

## 📥 Lambda Event Sample

This is the decoded JSON:

```json
{
  "username": "sai_preetham",
  "action": "login",
  "timestamp": "2025-07-25T14:00:00Z"
}
```

---

## 🧠 Learnt About

- Real-time streaming with AWS Kinesis
- Lambda integration with Kinesis
- Writing structured JSON data to DynamoDB
- Base64 encoding/decoding for AWS CLI
- Serverless architecture fundamentals

---

## ✅ Use Cases

- Logging user activity (login/logout)
- Real-time analytics ingestion
- Auditing and session tracking
- IoT event processing

---

## 📽️ Demo

[Click here to watch the demo](Demostration/Demo.mp4)

---

## 🤝 Author

**Sai Preetham**  
Cloud & Data Engineering Enthusiast ☁️  
[GitHub Profile](https://github.com/Preetham-Git005)

