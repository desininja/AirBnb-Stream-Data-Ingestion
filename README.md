---

# Airbnb Stream Data Ingestion

This repository implements a real-time data ingestion pipeline for Airbnb data using AWS services. The project leverages Lambda functions and other AWS technologies to produce, enrich, and consume data in a streaming architecture, providing scalability and efficient data processing.

## Architecture Overview

The pipeline consists of three key Lambda functions:

1. **Producer Lambda Function**: 
   - Responsible for generating and sending streaming data to a designated AWS service like Kinesis.

2. **Enrichment Lambda Function**: 
   - Processes incoming data to add additional information, perform transformations, or apply filtering.

3. **Consumer Lambda Function**: 
   - Consumes enriched data, storing it in a database or forwarding it for further analysis or visualization.

![Architecture Diagram](https://github.com/desininja/AirBnb-Stream-Data-Ingestion/blob/main/Architecture%20Diagram.drawio.png)


## Technologies Used

- **AWS Lambda**: For serverless data processing.
- **Amazon S3**: For data storage.
- **Amazon CloudWatch**: For monitoring and logging.

## Getting Started

### Prerequisites

- **AWS CLI** configured
- Basic knowledge of AWS Lambda, Kinesis, or similar streaming service

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/desininja/AirBnb-Stream-Data-Ingestion.git
   cd AirBnb-Stream-Data-Ingestion
   ```

2. Deploy the Lambda functions by following the deployment script or manual setup documentation provided in the repo.

3. Configure the necessary AWS services, such as IAM roles, Kinesis, and DynamoDB, as outlined in the setup guide.

## Usage

1. Trigger the **Producer Lambda** to initiate data streaming.
2. Observe the **Enrichment Lambda** processing the data in real-time.
3. Check the **Consumer Lambda** output to see the final processed data.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to suggest improvements or report bugs.

--- 
